# Generated by Django 3.2 on 2023-05-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0007_auto_20230508_0152"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyprofile",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]