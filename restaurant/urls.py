from django.urls import path
from .views import restaurant_view

urlpatterns = [
    path("", restaurant_view, name="map"),
]
