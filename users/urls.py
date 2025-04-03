from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login",),
    path("register/", views.register_view, name="register"),
    path('logout/', views.logout_view, name='logout'),
]