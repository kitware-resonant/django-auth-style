from django.contrib.sites.models import Site
from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains, assertNotContains
from pytest_mock import MockerFixture, MockType


@pytest.fixture
def site_middleware_disabled(mocker: MockerFixture) -> MockType:
    return mocker.patch(
        "django.contrib.sites.middleware.CurrentSiteMiddleware.process_request",
        return_value=None,
    )


def test_site_present(default_site: Site, client: Client):
    resp = client.get(reverse("account_login"))

    assert hasattr(resp.wsgi_request, "site")
    assertContains(resp, default_site.name, count=1, status_code=200)


def test_site_present_fallback(default_site: Site, client: Client, site_middleware_disabled):
    resp = client.get(reverse("account_login"))

    assert not hasattr(resp.wsgi_request, "site")
    assert "site" in resp.context
    assertContains(resp, default_site.name, count=1, status_code=200)


def test_site_absent(default_site: Site, user, client: Client, site_middleware_disabled):
    client.force_login(user)
    # This view doesn't pass "site" as context
    resp = client.get(reverse("account_logout"))

    assert "site" not in resp.context
    assertNotContains(resp, default_site.name, status_code=200)
