from django.urls import path

from places.views import retrieve_place

urlpatterns = [path("<int:place_id>/", retrieve_place)]
