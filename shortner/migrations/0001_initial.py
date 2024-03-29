# Generated by Django 5.0.1 on 2024-01-16 06:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortURL",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("original_url", models.URLField()),
                (
                    "short_part",
                    models.CharField(
                        max_length=20,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(15)],
                    ),
                ),
                ("expiration_date", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]
