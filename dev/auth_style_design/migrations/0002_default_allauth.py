from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps


def create_default_allauth(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor):
    User = apps.get_model("auth", "User")  # noqa: N806
    EmailAddress = apps.get_model("account", "EmailAddress")  # noqa: N806

    user = User.objects.create_user(
        username="user@auth-style-design.test",
        email="user@auth-style-design.test",
        password="password",
        first_name="John",
        last_name="Doe",
    )
    EmailAddress.objects.create(
        user=user,
        email=user.email,
        verified=True,
        primary=True,
    )


def delete_default_allauth(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor):
    User = apps.get_model("auth", "User")  # noqa: N806

    User.objects.filter(email="user@auth-style-design.test").delete()
    # EmailAddress will cascade delete


class Migration(migrations.Migration):
    dependencies = [
        ("auth_style_design", "0001_default_site"),
        # This is the final auth app migration
        ("auth", "0012_alter_user_first_name_max_length"),
        # This is the final account (Allauth) app migration
        ("account", "0002_email_max_length"),
    ]

    operations = [
        migrations.RunPython(create_default_allauth, delete_default_allauth),
    ]
