from django.shortcuts import render
from places.models import Place
from django.urls import reverse


def place_to_geojson(place: Place) -> dict:
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude],
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse("retrieve_place", args=[place.id]),
        },
    }


def show_start_page(request):
    """Render start page HTML
    Includes data about places on the map into HTML (not a good approach)
    """
    # Don't really like the idea of embedding the data into the page (not sure that's what was intended)
    # DRF with JSON would be much better (as in places/views.py)
    places = Place.objects.all()
    return render(
        request,
        "index.html",
        context={
            "geojson": {
                "type": "FeatureCollection",
                "features": [place_to_geojson(place) for place in places],
            }
        },
    )
