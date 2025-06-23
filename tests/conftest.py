from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Literal

from django.conf import settings
from django.test import Client
from django.urls import reverse
from playwright.sync_api import BrowserContext, Page
import pytest
from pytest_django.live_server_helper import LiveServer
from pytest_mock import MockerFixture, MockType
from pytest_playwright.pytest_playwright import CreateContextCallback

if TYPE_CHECKING:
    # Work around https://github.com/pytest-dev/pytest-django/issues/1152
    from allauth.socialaccount.models import SocialAccount
    from django.contrib.auth.models import User
    from django.contrib.sites.models import Site


@pytest.fixture(autouse=True)
def mock_generate_totp_secret(mocker: MockerFixture) -> MockType:
    return mocker.patch(
        "allauth.mfa.totp.internal.auth.generate_totp_secret",
        side_effect=lambda length=20: "A" * length,
    )


@pytest.fixture(autouse=True)
def mock_generate_seed(mocker: MockerFixture) -> MockType:
    return mocker.patch(
        "allauth.mfa.recovery_codes.internal.auth.RecoveryCodes.generate_seed",
        side_effect=lambda length=40: "A" * length,
    )


@pytest.fixture(autouse=True)
def default_site(transactional_db) -> Site:
    from django.contrib.sites.models import Site

    # The default site is created via the "post_migrate" signal and TransactionTestCase
    # specifically re-sends the "post_migrate" signal after flushing the database between each test.
    # So, the default site is guaranteed to exist for each test, but with its original value.
    site = Site.objects.get_current()
    site.domain = "localhost"
    site.name = "Django Auth Style"
    site.save()
    return site


@pytest.fixture
def mock_recently_authenticated(mocker: MockerFixture, settings) -> MockType:
    settings.ACCOUNT_REAUTHENTICATION_REQUIRED = True

    # Allauth MFA views do not respect the ACCOUNT_REAUTHENTICATION_REQUIRED setting
    return mocker.patch(
        "allauth.account.internal.flows.reauthentication.did_recently_authenticate",
        return_value=True,
    )


@pytest.fixture
def user(transactional_db) -> User:
    from django.contrib.auth.models import User

    return User.objects.create_user(
        username="test_user",
        first_name="Test",
        last_name="User",
        email="user@example.com",
        password="password",
    )


@pytest.fixture
def social_account(transactional_db, user) -> SocialAccount:
    from allauth.socialaccount.models import SocialAccount

    return SocialAccount.objects.create(
        user=user,
        provider="dummy",
        uid="1",
        extra_data={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
        },
    )


@pytest.fixture
def client() -> Client:
    return Client()


@pytest.fixture(params=["light", "dark"])
def color_scheme(request: pytest.FixtureRequest) -> Literal["light", "dark"]:
    return request.param


# This intentionally overrides the built-in fixture from pytest_playwright.
# This will also cause other built-in fixtures like "page" to have a base URL set.
@pytest.fixture
def context(live_server: LiveServer, new_context: CreateContextCallback) -> BrowserContext:
    context = new_context(base_url=live_server.url, device_scale_factor=1.0)
    context.set_default_timeout(3_000)
    return context


@pytest.fixture
def authenticated_context(context: BrowserContext, user: User) -> BrowserContext:
    # Using "Client.force_login" (then copying cookies to the browser) doesn't trigger all
    # the appropriate signals, so sessions aren't updated. Instead, login naively via
    # the browser.
    page = context.new_page()
    page.goto(reverse("account_login"))
    page.get_by_label("Username").fill(user.username)
    # The "user" object doesn't have the plain text password
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Sign In").click()
    # Ensure that pending messages are always rendered and cleared, which is more deterministic.
    page.wait_for_url(reverse(settings.LOGIN_REDIRECT_URL))
    page.close()

    return context


@pytest.fixture
def page(
    context: BrowserContext,
    color_scheme: Literal["light", "dark"],
) -> Page:
    page = context.new_page()
    page.emulate_media(color_scheme=color_scheme)
    return page


@pytest.fixture
def authenticated_page(
    authenticated_context: BrowserContext,
    color_scheme: Literal["light", "dark"],
) -> Page:
    page = authenticated_context.new_page()
    page.emulate_media(color_scheme=color_scheme)
    return page


@pytest.fixture
def assert_page_snapshot(assert_snapshot) -> Callable[[Page, str], None]:
    def _assert_page_snapshot(page: Page, view_name: str) -> None:
        assert_snapshot(
            page.screenshot(
                # full_page doesn't work: https://github.com/microsoft/playwright-python/issues/726
                full_page=True,
                # To make this reproducible, don't use the device DPI for scale
                scale="css",
                # There shouldn't be any animations, but disable for safety
                animations="disabled",
            ),
            threshold=0.3,
        )

    return _assert_page_snapshot
