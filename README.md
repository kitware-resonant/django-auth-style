# django-auth-style
[![PyPI](https://img.shields.io/pypi/v/django-auth-style)](https://pypi.org/project/django-auth-style/)

django-auth-style provides Django template styling for
[django-allauth](https://django-allauth.readthedocs.io/)
and [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/)
.

## Installation
### django-allauth Support
To enable support for django-allauth, install with:
```bash
pip install django-allauth django-auth-style[allauth]
```

Then enable the Django app:
```python
# settings.py
INSTALLED_APPS = [
    # Any project-local apps should come before "auth_style",
    # so templates can be overridden as needed
    'my_django_app.apps.MyDjangoAppConfig',
    ...,
    'auth_style',
    ...,
    # "allauth" must come after "auth_style"
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
```

### django-oauth-toolkit Support
To enable support for django-oauth-toolkit, install with:
```bash
pip install django-oauth-toolkit django-auth-style[oauth-toolkit]
```

Then enable the Django app:
```python
# settings.py
INSTALLED_APPS = [
    # Any project-local apps should come before "auth_style",
    # so templates can be overridden as needed
    'my_django_app.apps.MyDjangoAppConfig',
    ...,
    'auth_style',
    ...,
    # "oauth2_provider" must come after "auth_style"
    'oauth2_provider',
]
```

## Usage
When django-auth-style is properly installed alongside django-allauth or django-oauth-toolkit,
rendered templates will automatically be overridden with styled alternatives.
