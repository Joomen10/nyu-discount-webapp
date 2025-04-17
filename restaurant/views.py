from django.shortcuts import render, get_object_or_404, redirect
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
from django.contrib.auth.decorators import login_required
from django.utils.translation import override
from django.db.models import Avg

# importing needed restaurant model
from restaurant.models import Restaurants
from .forms import ReviewForm


# Changed home_view so that it brings real data from Restaurants model
def home_view(request):
    # 1) 각 식당의 평균 평점도 계산해서 가져옵니다.
    qs = Restaurants.objects.annotate(avg_rating=Avg("reviews__rating"))

    # 2) QuerySet 자체를 템플릿으로 넘겨줍니다.
    return render(
        request,
        "restaurant/home.html",
        {
            "restaurants": qs,
        },
    )


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


@login_required
def add_review(request, restaurant_pk):
    # 1) 해당 식당 가져오기
    restaurant = get_object_or_404(Restaurants, pk=restaurant_pk)

    # 2) 이미 내가 쓴 리뷰가 있으면 수정, 없으면 새로 생성
    try:
        review = Reviews.objects.get(restaurant=restaurant, user_id=request.user)
        form = ReviewForm(request.POST or None, instance=review)
    except Reviews.DoesNotExist:
        form = ReviewForm(request.POST or None)

    # 3) POST 요청 → 저장 후 리스트(또는 상세)로 리다이렉트
    if request.method == "POST" and form.is_valid():
        rev = form.save(commit=False)
        rev.restaurant_id = restaurant
        rev.user_id = request.user
        rev.save()
        return redirect("restaurant:home")

    # 4) GET 요청 → 폼 렌더링
    return render(
        request,
        "restaurant/add_review.html",
        {
            "restaurant": restaurant,
            "form": form,
        },
    )
