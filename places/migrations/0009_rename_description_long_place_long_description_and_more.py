# Generated by Django 4.1.4 on 2023-02-08 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0008_alter_placeimage_order_alter_placeimage_place"),
    ]

    operations = [
        migrations.RenameField(
            model_name="place",
            old_name="description_long",
            new_name="long_description",
        ),
        migrations.RenameField(
            model_name="place",
            old_name="description_short",
            new_name="short_description",
        ),
    ]