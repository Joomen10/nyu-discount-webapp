"""
URL configuration for nyudiscount project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, reverse
from . import views
from django.shortcuts import redirect


# 홈페이지로 들어가면 바로 로그인 페이지로 이동시키는 코딩
def redirect_to_login(request):
    return redirect("users:login")

urlpatterns = [
    path("admin/", admin.site.urls),
    # 아래것도 홈페이지로 들어가면 바로 로그인 페이지로 갈수 있게 해주는 코딩
    path("", redirect_to_login, name="home"),
    # 아래거 일단 삭제는 안함
    # path("", views.home_view, name="home"),
    path("map/", include("map.urls")),
    path('users/', include('users.urls')),
    path("restaurant/", include("restaurant.urls")),
    path("api/", include("restaurant.urls")),
]
