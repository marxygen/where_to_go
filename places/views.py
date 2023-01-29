from django.http import JsonResponse
from places.models import Place
from django.shortcuts import get_object_or_404


def jsonify_place(place: Place) -> dict:
    """Generate and return JSON representation"""
    # Usually DRF's Serializer / ModelSerializer are used for this purpose
    return {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": str(place.longitude), "lat": str(place.latitude)},
    }


def retrieve_place(request, place_id: int):
    place = get_object_or_404(Place, id=place_id)
    return JsonResponse(
        jsonify_place(place), json_dumps_params={"ensure_ascii": False, "indent": 2}
    )
