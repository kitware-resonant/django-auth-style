# Development

## Initial Setup
1. Install:
   1. [uv](https://docs.astral.sh/uv/getting-started/installation/)
   2. [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
   3. (Optional) [Watchman](https://facebook.github.io/watchman/docs/install)
2. Run `uv run dev/manage.py migrate`
3. Run `uv run dev/manage.py createsuperuser`
   and follow the prompts to create your own user
4. Run `npm install`
5. (Optional) run `uv sync --all-extras --all-groups` and configure your IDE to use
   `.venv/bin/python` as its interpreter.

## Run Application
1. In separate terminals, run both:
   1. `uv run dev/manage.py runserver`
   2. `npm run watch`
2. Access the site, starting at http://localhost:8000/
   * Outgoing emails are sent to the console
3. The Django admin interface is still available at http://localhost:8000/admin/
4. When finished, terminate with `Ctrl+C`

## Testing
1. Run `uv run tox`
2. Run `npm run lint`

### Updating Test Baselines
After any changes to the rendered appearance of templates, the test baselines must be updated:
1. Run `uv run tox -e test -- --update-snapshots`

### Detailed Template Coverage
To generate a detailed template coverage report for the tests:
1. Run `uv run tox -e test -- --cov-report html`
2. Open `htmlcov/index.html` in a web browser
