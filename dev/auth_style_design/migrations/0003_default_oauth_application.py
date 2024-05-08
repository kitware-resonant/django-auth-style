from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps


def create_default_oauth_application(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor):
    User = apps.get_model("auth", "User")  # noqa: N806
    Application = apps.get_model("oauth2_provider", "Application")  # noqa: N806

    user = User.objects.get(email="user@auth-style-design.test")
    Application.objects.create(
        user=user,
        redirect_uris="http://127.0.0.1:8000/ urn:ietf:wg:oauth:2.0:oob",
        client_type="public",  # Application.CLIENT_PUBLIC
        authorization_grant_type="authorization-code",  # Application.GRANT_AUTHORIZATION_CODE
        client_secret="",
        name="auth-style-design",
    )


def delete_default_oauth_application(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor):
    Application = apps.get_model("oauth2_provider", "Application")  # noqa: N806

    Application.objects.filter(name="auth-style-design").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("auth_style_design", "0002_default_allauth"),
        # This is the final auth app migration
        ("auth", "0012_alter_user_first_name_max_length"),
        # This is the final oauth2_provider app migration
        ("oauth2_provider", "0005_auto_20211222_2352"),
    ]

    operations = [
        migrations.RunPython(create_default_oauth_application, delete_default_oauth_application),
    ]
