from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

ROOT_URLCONF = "urls"
SECRET_KEY = "insecure-secret"
SITE_ID = 1

DEBUG = True
INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS = [
    "auth_style_design",
    "auth_style",
    "debug_toolbar",
    "django_browser_reload",
    "django.contrib.admin",
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
    "oauth2_provider",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
TIME_ZONE = "UTC"

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
# Django staticfiles auto-creates any intermediate directories, but do so here to prevent warnings.
STATIC_ROOT.mkdir(exist_ok=True)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_WEBAUTHN_ALLOW_INSECURE_ORIGIN = True
SOCIALACCOUNT_PROVIDERS = {
    "github": {"APP": {}},
    "google": {"APP": {}},
}

OAUTH2_PROVIDER = {
    "PKCE_REQUIRED": False,
    "ALLOWED_REDIRECT_URI_SCHEMES": ["http", "https"],
    "REQUEST_APPROVAL_PROMPT": "force",
}
