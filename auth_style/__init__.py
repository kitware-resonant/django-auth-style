import django

if django.VERSION < (3, 2):
    default_app_config = 'auth_style.apps.AuthStyleConfig'
