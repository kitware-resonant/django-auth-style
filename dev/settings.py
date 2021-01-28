from __future__ import annotations

from pathlib import Path
from typing import Type

from composed_configuration import (
    AllauthMixin,
    ComposedConfiguration,
    ConfigMixin,
    ConsoleEmailMixin,
    DebugMixin,
    DjangoMixin,
    LoggingMixin,
    StaticFileMixin,
)
from configurations import values


class MinimalDevelopmentBaseConfiguration(
    DebugMixin,
    ConsoleEmailMixin,
    LoggingMixin,
    AllauthMixin,
    StaticFileMixin,
    DjangoMixin,
    ComposedConfiguration,
):
    DEBUG = True
    SECRET_KEY = 'insecuresecret'
    ALLOWED_HOSTS = values.ListValue(['localhost', '127.0.0.1'])
    INTERNAL_IPS = ['127.0.0.1']

    OAUTH2_PROVIDER = {
        'PKCE_REQUIRED': True,
        'ALLOWED_REDIRECT_URI_SCHEMES': ['http', 'https'],
        'REQUEST_APPROVAL_PROMPT': 'force',
    }

    @staticmethod
    def before_binding(configuration: Type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += [
            'oauth2_provider',
        ]


class GirderStyleMixin(ConfigMixin):
    WSGI_APPLICATION = 'wsgi.application'
    ROOT_URLCONF = 'urls'

    BASE_DIR = Path(__file__).resolve(strict=True).parent

    DATABASES = {
        'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}
    }

    SITE_ID = 1

    @staticmethod
    def before_binding(configuration: ComposedConfiguration) -> None:
        configuration.INSTALLED_APPS += [
            'girder_style_design',
            'allauth.socialaccount.providers.github',
            'allauth.socialaccount.providers.google',
        ]

    # Force the logout confirm page to be rendered
    ACCOUNT_LOGOUT_ON_GET = False


class DevelopmentConfiguration(GirderStyleMixin, MinimalDevelopmentBaseConfiguration):
    pass
