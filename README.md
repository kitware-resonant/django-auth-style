# django-girder-style
[![PyPI](https://img.shields.io/pypi/v/django-girder-style)](https://pypi.org/project/django-girder-style/)

django-girder-style is a Django library providing styled versions of all
[django-allauth](https://django-allauth.readthedocs.io/)
and [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/)
view templates.

## Installation
### django-allauth Support
To enable support for django-allauth, install with:
```bash
pip install django-allauth django-girder-style[allauth]
```

Then enable the Django app:
```python
# settings.py
INSTALLED_APPS = [
    # Any project-local apps should come before "girder_style",
    # so templates can be overridden as needed
    'my_django_app.apps.MyDjangoAppConfig',
    ...,
    'girder_style',
    ...,
    # "allauth" must come after "girder_style"
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
```

### django-oauth-toolkit Support
To enable support for django-oauth-toolkit, install with:
```bash
pip install django-oauth-toolkit django-girder-style[oauth-toolkit]
```

Then enable the Django app:
```python
# settings.py
INSTALLED_APPS = [
    # Any project-local apps should come before "girder_style",
    # so templates can be overridden as needed
    'my_django_app.apps.MyDjangoAppConfig',
    ...,
    'girder_style',
    ...,
    # "oauth2_provider" must come after "girder_style"
    'oauth2_provider',
]
```

## Usage
When django-girder-style is properly installed alongside django-allauth or django-oauth-toolkit,
rendered templates will automatically be overridden with styled alternatives.
