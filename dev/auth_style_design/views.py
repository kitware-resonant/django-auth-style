from __future__ import annotations

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


template_file_groups = {
    "Allauth Initial Views": {
        "account_login": reverse_lazy("account_login"),
        "account_signup": reverse_lazy("account_signup"),
        "account_inactive": reverse_lazy("account_inactive"),
        "account_reset_password": reverse_lazy("account_reset_password"),
        "account_reset_password_done": reverse_lazy("account_reset_password_done"),
        "account_email_verification_sent": reverse_lazy("account_email_verification_sent"),
        # TODO: valid key
        "account_confirm_email (invalid)": reverse_lazy(
            "account_confirm_email", kwargs={"key": "secret-key"}
        ),
        # TODO: valid key
        "account_reset_password_from_key (invalid)": reverse_lazy(
            "account_reset_password_from_key", kwargs={"uidb36": "0", "key": "secret-key"}
        ),
        "account_reset_password_from_key_done": reverse_lazy(
            "account_reset_password_from_key_done"
        ),
    },
    "Allauth Logged-in Views": {
        "account_email": reverse_lazy("account_email"),
        "account_change_password": reverse_lazy("account_change_password"),
        "mfa_index": reverse_lazy("mfa_index"),
        "mfa_activate_totp": reverse_lazy("mfa_activate_totp"),
        "mfa_add_webauthn": reverse_lazy("mfa_add_webauthn"),
        "socialaccount_connections": reverse_lazy("socialaccount_connections"),
        "usersessions_list": reverse_lazy("usersessions_list"),
        "account_logout": reverse_lazy("account_logout"),
    },
    "Allauth Other Templates": {
        "account/verified_email_required.html": reverse_lazy(
            "auth-template-file", kwargs={"template_file": "verified_email_required.html"}
        ),
        "account/signup_closed.html": reverse_lazy(
            "auth-template-file", kwargs={"template_file": "signup_closed.html"}
        ),
    },
    "OAuth Toolkit Views": {
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
    },
}


def auth_template_listing(request):
    return render(
        request,
        "auth_style_design/auth_template_listing.html",
        {
            "template_file_groups": template_file_groups,
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
