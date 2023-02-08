# Generated by Django 4.1.4 on 2023-02-08 17:51

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0009_rename_description_long_place_long_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="long_description",
            field=tinymce.models.HTMLField(blank=True, verbose_name="Длинное описание"),
        ),
        migrations.AlterField(
            model_name="place",
            name="short_description",
            field=models.TextField(blank=True, verbose_name="Короткое описание"),
        ),
    ]
