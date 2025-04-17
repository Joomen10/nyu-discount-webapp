from django.urls import path
from .views import map_view, restaurant_list

urlpatterns = [
    path("", map_view, name="map"),
    path('api/restaurants/', restaurant_list, name='restaurant_list'),
    path('restaurants/', restaurant_list, name= 'restaurant_list')
    # /map/api/restaurants/ → 레스토랑 데이터 JSON 반환
]
