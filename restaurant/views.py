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


def register_view(request):
    with override("en"):  # 영어
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("login:login")  # 회원가입 후 이동할 URL
        else:
            form = UserCreationForm()
        return render(request, "restaurant/dj_register.html", {"form": form})


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
