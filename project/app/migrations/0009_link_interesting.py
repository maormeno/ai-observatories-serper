# Generated by Django 4.1.3 on 2022-12-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_alter_link_label_alter_link_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="link",
            name="interesting",
            field=models.BooleanField(null=True),
        ),
    ]
