from __future__ import annotations

from pathlib import Path

from composed_configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    HerokuProductionBaseConfiguration,
    ProductionBaseConfiguration,
    TestingBaseConfiguration,
)


class GirderAuthDesignConfig(ConfigMixin):
    WSGI_APPLICATION = 'girder_auth_design.wsgi.application'
    ROOT_URLCONF = 'girder_auth_design.urls'

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    SITE_ID = 1

    @staticmethod
    def before_binding(configuration: ComposedConfiguration) -> None:
        configuration.INSTALLED_APPS += [
            'girder_auth_design.core.apps.CoreConfig',
        ]


class DevelopmentConfiguration(GirderAuthDesignConfig, DevelopmentBaseConfiguration):
    pass


class TestingConfiguration(GirderAuthDesignConfig, TestingBaseConfiguration):
    pass


class ProductionConfiguration(GirderAuthDesignConfig, ProductionBaseConfiguration):
    pass


class HerokuProductionConfiguration(GirderAuthDesignConfig, HerokuProductionBaseConfiguration):
    pass
