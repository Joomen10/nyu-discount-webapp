from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Avg
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
from django.contrib.auth.decorators import login_required
from django.utils.translation import override
from django.db.models import Avg

# importing needed restaurant model
from restaurant.models import Restaurants


def home_view(request):
    # reviews__rating의 평균을 avg_rating으로 붙입니다.
    qs = Restaurants.objects.annotate(avg_rating=Avg("reviews__rating"))
    return render(request, "restaurant/home.html", {"restaurants": qs})


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
