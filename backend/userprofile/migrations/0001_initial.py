# Generated by Django 3.2 on 2023-03-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("website", models.URLField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="StudentAlumniProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_preference", models.CharField(max_length=100)),
                ("years_of_experience", models.IntegerField()),
                ("previous_employer", models.CharField(max_length=100)),
                ("linkedin_link", models.URLField()),
                ("github_link", models.URLField()),
            ],
        ),
    ]
