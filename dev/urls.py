from auth_style_design.views import auth_template_file, auth_template_listing
import debug_toolbar.toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    *debug_toolbar.toolbar.debug_toolbar_urls(),
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("oauth/", include("oauth2_provider.urls")),
    path("", auth_template_listing, name="auth-template-listing"),
    path("auth-template/<template_file>", auth_template_file, name="auth-template-file"),
]
