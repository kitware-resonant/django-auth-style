# Girder Auth Design

## Develop with Docker

Due to the dependency on npm and Python2, Docker development is the only supported
configuration.

### Initial Setup
1. Run `docker-compose run --rm django ./manage.py migrate`
2. Run `docker-compose run --rm django ./manage.py tailwind install`
3. Run `docker-compose run --rm django ./manage.py createsuperuser`
   and follow the prompts to create your own user

### Run Application
1. Run `docker-compose up`
2. Access the site, starting at http://localhost:8000/
   * Outgoing emails are sent to the console 
3. The Django admin interface is still available at http://localhost:8000/admin/
3. When finished, use `Ctrl+C`

### Application Maintenance
Occasionally, new package dependencies or schema changes will necessitate
maintenance. To non-destructively update your development stack at any time:
1. Run `docker-compose pull`
2. Run `docker-compose build`
3. Run `docker-compose run --rm django ./manage.py migrate`
4. Run `docker-compose run --rm django ./manage.py tailwind install`
