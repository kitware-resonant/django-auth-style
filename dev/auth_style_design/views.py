import urllib.parse

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from oauth2_provider.models import Application


def _oauth2_provider_authorize_url() -> str:
    base_url = reverse("oauth2_provider:authorize")
    qs = urllib.parse.urlencode(
        {
            "client_id": Application.objects.get(name="auth-style-design").client_id,
            "response_type": "code",
            # No redirect_uri required, it will use the value from the Application
            # Other arguments are optional to render a GET
        }
    )
    return f"{base_url}?{qs}"


def _oauth2_provider_authorize_oob_url() -> str:
    base_url = reverse("oauth2_provider:authorize")
    qs = urllib.parse.urlencode(
        {
            "client_id": Application.objects.get(name="auth-style-design").client_id,
            "response_type": "code",
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
            # Other arguments are optional to render a GET
        }
    )
    return f"{base_url}?{qs}"


template_files = {
    # Allauth
    "account/account_inactive.html": reverse_lazy("account_inactive"),
    "account/base.html": None,
    "account/email.html": reverse_lazy("account_email"),
    # TODO: valid key
    "account/email_confirm.html": reverse_lazy(
        "account_confirm_email", kwargs={"key": "secret-key"}
    ),  # invalid?
    "account/login.html": reverse_lazy("account_login"),
    "account/logout.html": reverse_lazy("account_logout"),  # broken
    "account/password_change.html": reverse_lazy("account_change_password"),  # redirects
    "account/password_reset.html": reverse_lazy("account_reset_password"),
    "account/password_reset_done.html": reverse_lazy("account_reset_password_done"),
    # TODO: valid key
    "account/password_reset_from_key.html": reverse_lazy(
        "account_reset_password_from_key", kwargs={"uidb36": "0", "key": "secret-key"}
    ),  # invalid?
    "account/password_reset_from_key_done.html": reverse_lazy(
        "account_reset_password_from_key_done"
    ),
    # 'account_set_password' redirects to 'account_change_password' if the user has a password
    # TODO: this doesn't render the form on the page
    "account/password_set.html": reverse_lazy(
        "auth-template-file", kwargs={"template_file": "password_set.html"}
    ),
    "account/signup.html": reverse_lazy("account_signup"),
    "account/signup_closed.html": reverse_lazy(
        "auth-template-file", kwargs={"template_file": "signup_closed.html"}
    ),
    "account/verification_sent.html": reverse_lazy("account_email_verification_sent"),
    "account/verified_email_required.html": reverse_lazy(
        "auth-template-file", kwargs={"template_file": "verified_email_required.html"}
    ),
    # OAuth Toolkit
    # https://django-oauth-toolkit.readthedocs.io/en/latest/templates.html
    "oauth2_provider/base.html": None,
    "oauth2_provider/authorize.html": _oauth2_provider_authorize_url,
    "oauth2_provider/authorize.html (invalid)": reverse_lazy("oauth2_provider:authorize"),
    "oauth2_provider/authorized-oob.html": _oauth2_provider_authorize_oob_url,
    # TODO: create a token for these to use
    # 'oauth2_provider/authorized-tokens.html': reverse_lazy(
    #     'oauth2_provider:authorized-token-list'
    # ),
    # 'oauth2_provider/authorized-token-delete.html': reverse_lazy(
    #     'oauth2_provider:authorized-token-delete', kwargs={'pk': 0}
    # ),
}


def auth_template_listing(request):
    return render(
        request,
        "auth_style_design/auth_template_listing.html",
        {
            "template_files": template_files,
        },
    )


def auth_template_file(request, template_file):
    # TODO: This is not used yet
    context = {}
    if template_file == "password_reset_done.html":
        context["user"] = {
            "is_authenticated": True,
        }
    return render(request, f"account/{template_file}", context)
