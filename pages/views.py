from django.shortcuts import render
from places.models import Place


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
                "features": [place.to_geojson() for place in places],
            }
        },
    )
