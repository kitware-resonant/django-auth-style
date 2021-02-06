FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Only copy the setup.py, it will still force all install_requires to be installed,
# but find_packages() will find nothing (which is fine). When Docker Compose mounts the real source
# over top of this directory, the .egg-link in site-packages resolves to the mounted directory
# and all package modules are importable.
COPY ./setup.py /opt/django-project/setup.py
COPY ./README.md /opt/django-project/README.md
RUN pip install --editable /opt/django-project

# Also install the requirements for the dev project
COPY ./dev/requirements.txt /opt/django-project/dev/requirements.txt
RUN pip install --requirement /opt/django-project/dev/requirements.txt

# Allow ./manage.py to auto-discover the girder_style_design app from the CWD
WORKDIR /opt/django-project/dev
