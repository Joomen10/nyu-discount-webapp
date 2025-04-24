from django.urls import path
from .views import map_view, restaurant_list

urlpatterns = [
    path("", map_view, name="map"),
]
