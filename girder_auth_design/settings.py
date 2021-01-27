from __future__ import annotations

from pathlib import Path

from composed_configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    TestingBaseConfiguration,
)


class GirderAuthDesignConfig(ConfigMixin):
    WSGI_APPLICATION = 'girder_auth_design.wsgi.application'
    ROOT_URLCONF = 'girder_auth_design.urls'

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    SITE_ID = 1

    @staticmethod
    def before_binding(configuration: ComposedConfiguration) -> None:
        # Insert before other apps with allauth templates
        auth_app_index = configuration.INSTALLED_APPS.index(
            'composed_configuration.authentication.apps.AuthenticationConfig'
        )
        configuration.INSTALLED_APPS.insert(auth_app_index, 'girder_auth_design.core.apps.CoreConfig')

        configuration.INSTALLED_APPS += [
            'tailwind',
            'girder_auth_design.theme',
            'allauth.socialaccount.providers.github',
            'allauth.socialaccount.providers.google',
            'allauth.socialaccount.providers.openid',
        ]

    TAILWIND_APP_NAME = 'girder_auth_design.theme'

    # Force the logout confirm page to be rendered
    ACCOUNT_LOGOUT_ON_GET = False

    SOCIALACCOUNT_PROVIDERS = {
        'openid': {
            'SERVERS': [
                dict(id='yahoo',
                     name='Yahoo',
                     openid_url='http://me.yahoo.com'),
                dict(id='hyves',
                     name='Hyves',
                     openid_url='http://hyves.nl'),
                dict(id='google',
                     name='Google',
                     openid_url='https://www.google.com/accounts/o8/id'),
            ]
        }
    }


class DevelopmentConfiguration(GirderAuthDesignConfig, DevelopmentBaseConfiguration):
    pass


class TestingConfiguration(GirderAuthDesignConfig, TestingBaseConfiguration):
    pass
