# Generated by Django 4.1.4 on 2023-01-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Layoff", "Layoff"),
                            ("Hiring", "Hiring"),
                            ("Hiring Frozen", "Hiring Frozen"),
                        ],
                        default="Hiring",
                        max_length=20,
                    ),
                ),
                ("last_updated", models.DateField(blank=True, null=True)),
                ("application_link", models.URLField(blank=True)),
                ("notes", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
