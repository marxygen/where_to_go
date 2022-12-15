# Generated by Django 4.1.4 on 2022-12-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description_short",
                    models.TextField(verbose_name="Короткое описание"),
                ),
                ("description_long", models.TextField(verbose_name="Длинное описание")),
                (
                    "latitude",
                    models.DecimalField(
                        decimal_places=16, max_digits=22, verbose_name="Широта"
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        decimal_places=16, max_digits=22, verbose_name="Долгота"
                    ),
                ),
            ],
            options={
                "verbose_name": "Место",
                "verbose_name_plural": "Места",
            },
        ),
    ]