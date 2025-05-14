from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_template_base_used(client: Client):
    with assertTemplateUsed("auth_style/base.html", count=1):
        client.get(reverse("account_login"))
