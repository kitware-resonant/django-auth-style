# django-girder-style
[![PyPI](https://img.shields.io/pypi/v/django-girder-style)](https://pypi.org/project/django-girder-style/)

django-girder-style is a Django library providing
styled Django templates for data management applications.


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

Enable django-girder-style as an installed Django app:
```python
# settings.py
INSTALLED_APPS = [
    # Any project-local apps should come before "girder_style",
    # so templates can be overridden as needed
    'my_django_app.apps.MyDjangoAppConfig',
    ...,
    'girder_style',
    ...,
    # If "allauth" is installed, it must come after "girder_style"
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
```

## Usage
### Base Template
All project templates
[should extend](https://docs.djangoproject.com/en/3.1/ref/templates/language/#template-inheritance)
`base.html`.
This provides the following blocks to inject content:
* `head_title`: The content of the `<title>` tag.
* `extra_head`: Additional HTML placed within the `<head>` tag.
* `body`: The entire HTML body content, including the `<body>` tag itself.

For example, a template `my_app/home.html` may contain:
```html
{% extends 'base.html' %}

{% block head_title %}My App{% endblock %}

{% block extra_head %}
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
{% endblock %}

{% block body %}
<body>
  <div>Hello World.</div>
</body>
{% endblock %}
```

### django-allauth Templates
When django-girder-style is properly installed with django-allauth, templates will automatically
be overridden with styled alternatives.
