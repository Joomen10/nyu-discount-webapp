from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsersViewSet,
    RestaurantsViewSet,
    MenusViewSet,
    DiscountsViewSet,
    ReviewsViewSet,
)
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

router = DefaultRouter()
router.register(r"users", UsersViewSet)
router.register(r"restaurants", RestaurantsViewSet)
router.register(r"menus", MenusViewSet)
router.register(r"discounts", DiscountsViewSet)
router.register(r"reviews", ReviewsViewSet)

app_name = "restaurant"

urlpatterns = [
    path("", views.home_view, name="home"),
]

""" 초반에 일반적인 login 페이지 만드느 방식으로 했는데 자꾸 안되길래 알아봤더니 router? 이거 때문에 "내부에서는 Django Rest Framework(DRF)의 Router 기반 URL 패턴만 노출되고 있습니다. 
즉, 일반 Django 뷰용 URL(예: 로그인 페이지 경로)이 전혀 정의되지 않았거나, DRF 라우터에 가려져서 매칭되지 않고 있는 상황입니다.
결과적으로 /restaurant/login/ 요청을 받을 만한 URL 패턴이 전혀 없으니 “Page not found”가 뜨는 것입니다." 라네요
그래서 밑에 코딩을 하나 추가해줬습니다
"""
# 마지막에 DRF 라우터가 자동 생성한 URL들을 포함
urlpatterns += router.urls
