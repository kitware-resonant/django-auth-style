# django-girder-style
[![PyPI](https://img.shields.io/pypi/v/django-girder-style)](https://pypi.org/project/django-girder-style/)

django-girder-style is a Django library providing
Django template styling for Girder-4 applications.

_Note: The `django-girder-style` package is deprecated;
it has been superseded by `django-auth-style`._

### Benefits
django-girder-style provides an extensible block-oriented base HTML template.
This base template includes
a pre-built [Tailwind CSS](https://tailwindcss.com/) (with some minor customizations) stylesheet,
[Remix Icon](https://remixicon.com/) support,
and the [Nunito](https://fonts.google.com/specimen/Nunito) font.

Additionally, django-girder-style provides styled versions of all
[django-allauth](https://django-allauth.readthedocs.io/) view templates.
This styling allows some limited branding customization as well.

## Installation
Install django-girder-style:
```bash
pip install django-girder-style
```

### django-allauth Support
To enable support for [django-allauth](https://django-allauth.readthedocs.io/),
install with:
```bash
pip install django-girder-style[allauth]
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
To enable support for [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/),
install with:
```bash
pip install django-girder-style[oauth-toolkit]
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
    # If "oauth2_provider" is installed, it must come after "girder_style"
    'oauth2_provider',
]
```

## Usage
### Base Template
All project templates
[should extend](https://docs.djangoproject.com/en/3.1/ref/templates/language/#template-inheritance)
`girder_style/base.html`.
This provides the following blocks to inject content:
* `head_title`: The content of the `<title>` tag.
* `head_extra`: Additional HTML placed within the `<head>` tag.
* `body`: The entire HTML body content, including the `<body>` tag itself.

For example, a template `my_app/home.html` may contain:
```django
{% extends 'girder_style/base.html' %}

{% block head_title %}My App{% endblock %}

{% block head_extra %}
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
{% endblock %}

{% block body %}
<body>
  <div style="font-bold">Hello World.</div>
  <i class="ri-hearts-fill"></i>
</body>
{% endblock %}
```

All basic [Tailwind CSS](https://tailwindcss.com/) classes are available for use in templates
extending `girder_style/base.html`, as illustrated in the example above.
No additional configuration of Tailwind CSS is required (or possible).
For a full list of the additional Tailwind CSS customizations applied by django-girder-style,
see [the Tailwind CSS confile file](tailwind/tailwind.config.js) and
[the stylesheet](tailwind/src/styles.scss).

The [Remix Icon](https://remixicon.com/) library is also available in the same way.
Icons are typically used by adding an `<i class="ri-...` element, but see
[the Remix Icon documentation](https://github.com/Remix-Design/remixicon#use) for full usage
information.

### django-allauth Templates
When django-girder-style is properly installed with django-allauth, templates will automatically
be overridden with styled alternatives.
