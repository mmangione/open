# Generated by Django 2.2.13 on 2020-07-06 12:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0007_create_betterself_models_p2"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UserSupplementStack", new_name="SupplementStack",
        ),
        migrations.RenameModel(
            old_name="UserSupplementStackComposition",
            new_name="SupplementStackComposition",
        ),
    ]
