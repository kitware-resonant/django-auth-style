import warnings

import django

if django.VERSION < (3, 2):
    default_app_config = 'girder_style.apps.GirderStyleConfig'


warnings.warn(
    'The django-girder-style package is deprecated; it has been superseded by django-auth-style.',
    DeprecationWarning,
)
