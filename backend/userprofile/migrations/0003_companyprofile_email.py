# Generated by Django 3.2 on 2023-04-17 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0002_studentalumniprofile_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="companyprofile",
            name="email",
            field=models.EmailField(default="", max_length=255, unique=True),
        ),
    ]
