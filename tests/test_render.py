from __future__ import annotations

from typing import TYPE_CHECKING

from allauth.mfa.recovery_codes.internal import auth as recovery_codes_auth
from allauth.mfa.totp.internal import auth as totp_auth
from allauth.mfa.webauthn.internal.auth import WebAuthn
from django.urls import reverse
from freezegun import freeze_time
import pytest

if TYPE_CHECKING:
    from allauth.socialaccount.models import SocialAccount
    from django.contrib.auth.models import User
    from playwright.sync_api import Page
    from pytest_django.fixtures import SettingsWrapper
    from pytest_playwright_visual_snapshot.plugin import AssertSnapshot


def test_render_base_messages(authenticated_page: Page, assert_snapshot: AssertSnapshot) -> None:
    authenticated_page.goto(reverse("test_add_messages"))
    authenticated_page.goto(reverse("account_logout"))

    # The font needs to be downloaded from the web
    authenticated_page.evaluate("document.fonts.ready")
    assert_snapshot(authenticated_page)


@pytest.mark.parametrize(
    "view_name",
    [
        # Initial views
        "account_login",
        "account_signup",
    ],
)
def test_render_logged_out(view_name: str, page: Page, assert_snapshot: AssertSnapshot) -> None:
    page.goto(reverse(view_name))

    # The font needs to be downloaded from the web
    page.evaluate("document.fonts.ready")
    assert_snapshot(page)


def test_render_non_form_errors(user: User, page: Page, assert_snapshot: AssertSnapshot) -> None:
    page.goto(reverse("account_login"))
    page.get_by_label("Username").fill(user.username)
    page.get_by_label("Password").fill("wrong_password")
    page.get_by_role("button", name="Sign In").click()

    # The font needs to be downloaded from the web
    page.evaluate("document.fonts.ready")
    assert_snapshot(page)


@pytest.mark.parametrize(
    "view_name",
    [
        # Views in the logged-in menu
        "account_email",
        "account_change_password",
        "mfa_index",
        "usersessions_list",
        "socialaccount_connections",
        "account_logout",
        # View with an "img" element
        "mfa_activate_totp",
    ],
)
def test_render_logged_in(
    view_name: str, authenticated_page: Page, assert_snapshot: AssertSnapshot
) -> None:
    authenticated_page.goto(reverse(view_name))

    # The font needs to be downloaded from the web
    authenticated_page.evaluate("document.fonts.ready")
    assert_snapshot(authenticated_page)


def test_render_with_field_textarea(
    user: User, authenticated_page: Page, assert_snapshot: AssertSnapshot
) -> None:
    # Must do this after "authenticated_page" is created, or login will require MFA
    totp_auth.TOTP.activate(user, totp_auth.generate_totp_secret())
    recovery_codes_auth.RecoveryCodes.activate(user)

    authenticated_page.goto(reverse("mfa_view_recovery_codes"))

    # The font needs to be downloaded from the web
    authenticated_page.evaluate("document.fonts.ready")
    assert_snapshot(authenticated_page)


def test_render_with_field_radio(
    social_account: SocialAccount,
    authenticated_page: Page,
    assert_snapshot: AssertSnapshot,
) -> None:
    authenticated_page.goto(reverse("socialaccount_connections"))

    # The font needs to be downloaded from the web
    authenticated_page.evaluate("document.fonts.ready")
    assert_snapshot(authenticated_page)


def test_render_with_button_edit(
    user: User, authenticated_page: Page, assert_snapshot: AssertSnapshot
) -> None:
    # Create WebAuthn Authenticator here, so it's not prompted during the login flow
    with freeze_time("2026-01-01"):
        WebAuthn.add(
            user=user,
            name="WebAuthn key",
            credential={},
        )

    authenticated_page.goto(reverse("mfa_list_webauthn"))

    # The font needs to be downloaded from the web
    authenticated_page.evaluate("document.fonts.ready")
    assert_snapshot(authenticated_page)


@pytest.mark.parametrize("details_open", [False, True], ids=["closed", "open"])
def test_render_with_element_details(
    settings: SettingsWrapper,
    page: Page,
    assert_snapshot: AssertSnapshot,
    *,
    details_open: bool,
) -> None:
    # The following are all required to render a details element
    settings.ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    settings.ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
    settings.ACCOUNT_EMAIL_VERIFICATION_SUPPORTS_CHANGE = True
    # Make the email field required
    settings.ACCOUNT_SIGNUP_FIELDS = ["username*", "email*", "password1*", "password2*"]

    page.goto(reverse("account_signup"))
    page.get_by_label("Username").fill("test_user")
    page.get_by_label("Email").fill("user@example.com")
    page.get_by_label("Password", exact=True).fill("T3st_passw0rd!")
    page.get_by_label("Password (again)").fill("T3st_passw0rd!")
    page.get_by_role("button", name="Sign Up").click()

    if details_open:
        page.get_by_text("different email address").click()
        page.get_by_role("button", name="Change").wait_for()
        # Opening the pane triggers an animation
        page.evaluate("Promise.all(document.getAnimations().map(a => a.finished))")

    # The font needs to be downloaded from the web
    page.evaluate("document.fonts.ready")
    assert_snapshot(page)


def test_render_override_style(
    override_app_style: None, page: Page, assert_snapshot: AssertSnapshot
) -> None:
    """Test that template overrides are applied and render correctly with custom styling."""
    page.goto(reverse("account_login"))

    # The font needs to be downloaded from the web
    page.evaluate("document.fonts.ready")
    assert_snapshot(page)
