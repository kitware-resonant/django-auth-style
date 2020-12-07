from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from girder_auth_design.core.views import auth_template, auth_template_listing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', auth_template_listing, name='auth-template-listing'),
    path('auth/<template_file>', auth_template, name='auth-template'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
