# Generated by Django 4.1.3 on 2022-11-21 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_link_options_alter_link_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="link",
            old_name="source",
            new_name="url",
        ),
    ]