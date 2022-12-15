from django.http import JsonResponse
from places.models import Place
from django.shortcuts import get_object_or_404


def retrieve_place(request, place_id: int):
    place = get_object_or_404(Place, id=place_id)
    return JsonResponse(place.jsonify(), json_dumps_params={'ensure_ascii': False, 'indent': 2})
