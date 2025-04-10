from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings  # nyudiscount의 settings에서 가져옴
from restaurant.models import Restaurants

def map_view(request):
    context = {
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, "map/map.html", context)

def restaurant_list(request):
    qs = Restaurants.objects.all()
    data = [
        {
            "name": r.name,
            "address": r.address,
            "lat": float(r.latitude) if r.latitude else None,
            "lng": float(r.longitude) if r.longitude else None,
            "rating": float(r.rating) if r.rating else None,
        } for r in qs
    ]
    return JsonResponse(data, safe=False)
