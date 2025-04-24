# restaurant/api_urls.py (새로 추가)
from django.urls import path
from . import views

app_name = "restaurant_api"

urlpatterns = [
    path("signup/", views.signup_api, name="signup"),
]
