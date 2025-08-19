from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_template_base_used(client: Client):
    with assertTemplateUsed("auth_style/base.html", count=1):
        client.get(reverse("account_login"))


@pytest.mark.django_db
def test_template_override_applied(settings, client: Client):
    # Configure settings directly in the test
    settings.INSTALLED_APPS = [
        "test_override_app.auth_style_design",
        "auth_style",
        *[
            app
            for app in settings.INSTALLED_APPS
            if app not in {"test_override_app.auth_style_design", "auth_style"}
        ],
    ]
)
def test_template_override_applied(client: Client):
    with assertTemplateUsed("auth_style/site_name.html", count=1):
        response = client.get(reverse("account_login"))
    assert "🚀 My Custom App" in response.content.decode()
