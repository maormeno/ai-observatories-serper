# Generated by Django 4.1.3 on 2022-11-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_link_created_at_link_updated_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="link",
            options={"select_on_save": True},
        ),
        migrations.AlterField(
            model_name="link",
            name="created_at",
            field=models.DateField(default=None, null=True),
        ),
    ]
