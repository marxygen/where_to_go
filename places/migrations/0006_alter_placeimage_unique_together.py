# Generated by Django 4.1.4 on 2022-12-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0005_alter_place_description_long"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="placeimage",
            unique_together={("title", "image", "place", "order")},
        ),
    ]
