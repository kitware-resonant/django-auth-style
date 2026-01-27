from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains, assertTemplateUsed


@pytest.mark.django_db
def test_template_base_used(client: Client) -> None:
    with assertTemplateUsed("auth_style/base.html", count=1):
        client.get(reverse("account_login"))


@pytest.mark.django_db
def test_template_override_applied(override_app_style: None, client: Client) -> None:
    response = client.get(reverse("account_login"))
    assertContains(response, "🚀 My Custom App")
