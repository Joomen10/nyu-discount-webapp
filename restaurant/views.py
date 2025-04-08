from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Users, Restaurants, Menus, Discounts, Reviews
from .serializers import (
    UsersSerializer,
    RestaurantsSerializer,
    MenusSerializer,
    DiscountsSerializer,
    ReviewsSerializer,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.translation import override

 # 식당 리스트 예시. 실제 레스토랑을 map에서 import 해야됨.
restaurantList = [
    {'name': 'Pizza Place', 'location': 'Downtown'},
    {'name': 'Sushi Spot', 'location': 'Uptown'},
    {'name': 'Burger Joint', 'location': 'Suburbs'},
    {'name': 'Taco Truck', 'location': 'East Side'},
    {'name': 'Pasta Corner', 'location': 'West Side'},
    {'name': 'Pizza Place', 'location': 'Downtown'},
    {'name': 'Sushi Spot', 'location': 'Uptown'},
    {'name': 'Burger Joint', 'location': 'Suburbs'},
    {'name': 'Taco Truck', 'location': 'East Side'},
    {'name': 'Pasta Corner', 'location': 'West Side'},
    {'name': 'Pizza Place', 'location': 'Downtown'},
    {'name': 'Sushi Spot', 'location': 'Uptown'},
    {'name': 'Burger Joint', 'location': 'Suburbs'},
    {'name': 'Taco Truck', 'location': 'East Side'},
    {'name': 'Pasta Corner', 'location': 'West Side'},
]

def home_view(request):
    return render(request, 'restaurant/home.html', {'restaurantList': restaurantList})

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class RestaurantsViewSet(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


class MenusViewSet(viewsets.ModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer


class DiscountsViewSet(viewsets.ModelViewSet):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
