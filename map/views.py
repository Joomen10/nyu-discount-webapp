from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def map_view(request):
    return HttpResponse("Hello, this is the map view!")
