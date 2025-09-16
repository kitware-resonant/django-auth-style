from allauth.mfa.recovery_codes.internal import auth as recovery_codes_auth
from allauth.mfa.totp.internal import auth as totp_auth
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.urls import reverse
from playwright.sync_api import Page
import pytest


def test_render_base_messages(authenticated_page: Page, assert_page_snapshot) -> None:
    authenticated_page.goto(reverse("test_add_messages"))
    authenticated_page.goto(reverse("account_logout"))

    assert_page_snapshot(authenticated_page, "messages")


@pytest.mark.parametrize(
    "view_name",
    [
        # Initial views
        "account_login",
        "account_signup",
    ],
)
def test_render_logged_out(view_name: str, page: Page, assert_page_snapshot) -> None:
    page.goto(reverse(view_name))

    assert_page_snapshot(page, view_name)


def test_render_non_form_errors(user: User, page: Page, assert_page_snapshot) -> None:
    page.goto(reverse("account_login"))
    page.get_by_label("Username").fill(user.username)
    page.get_by_label("Password").fill("wrong_password")
    page.get_by_role("button", name="Sign In").click()

    assert_page_snapshot(page, "non_form_errors")


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
def test_render_logged_in(view_name: str, authenticated_page: Page, assert_page_snapshot) -> None:
    authenticated_page.goto(reverse(view_name))

    assert_page_snapshot(authenticated_page, view_name)


def test_render_with_field_textarea(
    user: User, authenticated_page: Page, assert_page_snapshot
) -> None:
    # Must do this after "authenticated_page" is created, or login will require MFA
    totp_auth.TOTP.activate(user, totp_auth.generate_totp_secret())
    recovery_codes_auth.RecoveryCodes.activate(user)

    view_name = "mfa_view_recovery_codes"
    authenticated_page.goto(reverse(view_name))

    assert_page_snapshot(authenticated_page, view_name)


def test_render_with_field_radio(
    social_account: SocialAccount, authenticated_page: Page, assert_page_snapshot
) -> None:
    view_name = "socialaccount_connections"
    authenticated_page.goto(reverse(view_name))

    assert_page_snapshot(authenticated_page, f"{view_name}_set")


@pytest.mark.parametrize("view_name", ["account_login"])
def test_render_override_style(
    override_app_style, view_name: str, page: Page, assert_page_snapshot
) -> None:
    """Test that template overrides are applied and render correctly with custom styling."""
    page.goto(reverse(view_name))
    assert_page_snapshot(page, view_name)
