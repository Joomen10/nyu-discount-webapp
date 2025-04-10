from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsersViewSet,
    RestaurantsViewSet,
    MenusViewSet,
    DiscountsViewSet,
    ReviewsViewSet,
    LoginView,
    LogoutView,  # Your API view
    register_view,
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

app_name = 'restaurant_app'

urlpatterns = [
    # Custom login page using Django's built-in view
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    
    # Django built-in logout that redirects to login page
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/restaurant/login/"),
        name="logout",
    ),
    
    # Register view
    path("register/", register_view, name="register"),
    
    # API login/logout (optional if you are also providing DRF-based authentication)
    path("api/login/", LoginView.as_view(), name="api-login"),
    path("api/logout/", LogoutView.as_view(), name="api-logout"),
    
    # DRF router URLs
    path("api/", include(router.urls)),
]
urlpatterns += router.urls