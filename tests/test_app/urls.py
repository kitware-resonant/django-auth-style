from django.urls import include, path

from . import views

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("test/messages/", views.add_messages, name="test_add_messages"),
]
