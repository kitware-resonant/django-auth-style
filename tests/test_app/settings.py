ROOT_URLCONF = "test_app.urls"
SECRET_KEY = "insecure-secret"
SITE_ID = 1

INSTALLED_APPS = [
    "auth_style",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.mfa",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.dummy",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
    "allauth.usersessions",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # Necessary for django_coverage_plugin
            "debug": True,
        },
    },
]

# The default '/accounts/profile/' doesn't exist, and this is a reasonable location
LOGIN_REDIRECT_URL = "usersessions_list"

# Increase coverage by enabling functionality
ACCOUNT_LOGIN_BY_CODE_ENABLED = True

SOCIALACCOUNT_PROVIDERS: dict[str, dict] = {
    "github": {"APP": {}},
    "google": {"APP": {}},
}
