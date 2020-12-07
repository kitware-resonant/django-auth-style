release: ./manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT girder_auth_design.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery --app girder_auth_design.celery worker --loglevel INFO --without-heartbeat
