from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from allauth.usersessions.models import UserSession
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.test import Client
import pytest

if TYPE_CHECKING:
    from playwright.sync_api import BrowserContext, Page
    from pytest_django.fixtures import SettingsWrapper
    from pytest_django.live_server_helper import LiveServer
    from pytest_mock import MockerFixture, MockType
    from pytest_playwright.pytest_playwright import CreateContextCallback


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
def default_site(transactional_db: None) -> Site:
    # The default site is created via the "post_migrate" signal and TransactionTestCase
    # specifically re-sends the "post_migrate" signal after flushing the database between each test.
    # So, the default site is guaranteed to exist for each test, but with its original value.
    site = Site.objects.get_current()
    site.domain = "localhost"
    site.name = "Django Auth Style"
    site.save()
    return site


@pytest.fixture
def mock_recently_authenticated(mocker: MockerFixture, settings: SettingsWrapper) -> MockType:
    settings.ACCOUNT_REAUTHENTICATION_REQUIRED = True

    # Allauth MFA views do not respect the ACCOUNT_REAUTHENTICATION_REQUIRED setting
    return mocker.patch(
        "allauth.account.internal.flows.reauthentication.did_recently_authenticate",
        return_value=True,
    )


@pytest.fixture
def user(transactional_db: None) -> User:
    user = User.objects.create_user(
        username="test_user",
        first_name="Test",
        last_name="User",
        email="user@example.com",
        password="T3st_passw0rd!",
    )
    # Having a confirmed user helps to increase test coverage by showing additional badges
    EmailAddress.objects.create(
        user=user,
        email=user.email,
        verified=True,
        primary=True,
    )
    return user


@pytest.fixture
def social_account(transactional_db: None, user: User) -> SocialAccount:
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
    return request.param  # type: ignore[no-any-return]


_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "HeadlessChrome/136.0.7103.25 "
    "Safari/537.36"
)


# This intentionally overrides the built-in fixture from pytest_playwright.
# Normalize rendering to reduce differences between local and CI environments.
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict[str, Any]) -> dict[str, Any]:
    return {
        **browser_type_launch_args,
        "args": [
            "--font-render-hinting=none",
            "--force-color-profile=srgb",
        ],
    }


# This intentionally overrides the built-in fixture from pytest_playwright.
# This will also cause other built-in fixtures like "page" to have a base URL set.
@pytest.fixture
def context(live_server: LiveServer, new_context: CreateContextCallback) -> BrowserContext:
    context = new_context(
        base_url=live_server.url,
        device_scale_factor=1.0,
        # Lock the reported user agent, as the usersessions_list renders it
        user_agent=_USER_AGENT,
    )
    context.set_default_timeout(3_000)
    return context


@pytest.fixture
def authenticated_context(
    context: BrowserContext,
    client: Client,
    user: User,
    mock_recently_authenticated: MockType,
) -> BrowserContext:
    # Use force_login + cookie injection instead of filling the login form for speed.
    client.force_login(user)
    session_cookie = client.cookies[settings.SESSION_COOKIE_NAME]
    UserSession.objects.create(
        user=user,
        session_key=client.session.session_key,
        ip="127.0.0.1",
        user_agent=_USER_AGENT,
    )
    context.add_cookies(
        [
            {
                "name": session_cookie.key,
                "value": session_cookie.value,
                "domain": "localhost",
                "path": "/",
            }
        ]
    )
    return context


def _new_page(context: BrowserContext, color_scheme: Literal["light", "dark"]) -> Page:
    page = context.new_page()
    page.emulate_media(color_scheme=color_scheme)
    page.set_default_timeout(3_000)
    return page


@pytest.fixture
def page(context: BrowserContext, color_scheme: Literal["light", "dark"]) -> Page:
    return _new_page(context, color_scheme)


@pytest.fixture
def authenticated_page(
    authenticated_context: BrowserContext, color_scheme: Literal["light", "dark"]
) -> Page:
    return _new_page(authenticated_context, color_scheme)


@pytest.fixture
def override_app_style(settings: SettingsWrapper) -> None:
    settings.INSTALLED_APPS = ["test_override_app.auth_style_design", *settings.INSTALLED_APPS]
