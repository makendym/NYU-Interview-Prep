# Generated by Django 3.2 on 2023-05-03 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Aggregations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("last_agg_id", models.IntegerField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserWiseAggregation",
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
                ("agg_id", models.IntegerField()),
                ("num_exp_posted", models.IntegerField()),
                ("num_rec_posted", models.IntegerField()),
                ("num_codes_posted", models.IntegerField()),
                ("num_totalcmnts_posted", models.IntegerField()),
                ("num_expcmnts_posted", models.IntegerField()),
                ("num_anscmnts_posted", models.IntegerField()),
                ("avg_rec_rating_received", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]