from __future__ import annotations

from typing import TYPE_CHECKING

from django.urls import reverse
from playwright.sync_api import expect

if TYPE_CHECKING:
    from playwright.sync_api import BrowserContext


def test_form_checkbox_state_survives_failed_submit(context: BrowserContext) -> None:
    page = context.new_page()
    page.goto(reverse("account_login"))
    remember = page.get_by_role("checkbox", name="Remember Me")

    page.get_by_label("Username").fill("nonexistent_user")
    page.get_by_label("Password").fill("wrong_password")
    remember.check()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_text("not correct").wait_for()

    expect(remember).to_be_checked()
    # A "value" attribute would be posted in place of the default "on", which Django's
    # CheckboxInput could misread (e.g. "False" is parsed as unchecked)
    expect(remember).not_to_have_attribute("value")
