from django.core.management.base import BaseCommand
import requests
from places.models import Place, PlaceImage
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = "Load information about a place from specified JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--url", required=True, help="Path to JSON file with place details"
        )

    def handle(self, *args, **options):
        url = options.get("url")
        if not url:
            raise ValueError(f"You must specify a URL to JSON file!")

        r = requests.get(url)
        r.raise_for_status()
        contents = r.json()

        images = contents.get("imgs", [])
        coordinates = contents.get("coordinates")
        data = {
            'latitude': coordinates["lat"],
            'longitude': coordinates["lng"],
            'short_description': coordinates.get('description_short'),
            'long_description': coordinates.get('description_long')
        }
        place, created = Place.objects.update_or_create(
            title=contents.pop("title"), defaults=data
        )

        if not created:
            print(f"Place {place.title} already exists")
            place.images.all().delete()

        for index, image_url in enumerate(images):
            print(f"Processing image #{index+1}", end="\r")
            PlaceImage.objects.get_or_create(
                order=index,
                place=place,
                image=ContentFile(
                    requests.get(image_url).content, name=image_url.split("/")[-1]
                ),
            )

        print(f"{'Added' if created else 'Updated'} place {place.title}")
