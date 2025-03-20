from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import (
    UsersViewSet,
    RestaurantsViewSet,
    MenusViewSet,
    DiscountsViewSet,
    ReviewsViewSet,
    LoginView, 
    LogoutView,  
    register_view, 
)

app_name = "restaurant_app"

# ✅ DRF Router Setup
router = DefaultRouter()
router.register(r"users", UsersViewSet)
router.register(r"restaurants", RestaurantsViewSet)
router.register(r"menus", MenusViewSet)
router.register(r"discounts", DiscountsViewSet)
router.register(r"reviews", ReviewsViewSet)

# ✅ Web-based login/logout
urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="restaurant/dj_login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/restaurant/login/"), 
        name="logout",
    ),
    path("register/", register_view, name="register"),
]

# ✅ API-based login/logout (Token Authentication)
urlpatterns += [
    path("api/login/", LoginView.as_view(), name="api-login"),  # API login
    path("api/logout/", LogoutView.as_view(), name="api-logout"),  # API logout
]

# ✅ Include DRF API routes
urlpatterns += router.urls
