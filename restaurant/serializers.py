from rest_framework import serializers
from .models import Users, Restaurants, Menus, Discounts, Reviews

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # Includes all fields from the model

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'

class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'