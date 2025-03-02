from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, RestaurantsViewSet, MenusViewSet, DiscountsViewSet, ReviewsViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'restaurants', RestaurantsViewSet)
router.register(r'menus', MenusViewSet)
router.register(r'discounts', DiscountsViewSet)
router.register(r'reviews', ReviewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
