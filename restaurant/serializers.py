from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from .models import Users, Restaurants, Menus, Discounts, Reviews

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])  # Hide password in responses

    class Meta:
        model = Users
        fields = ['user_id', 'name', 'email', 'password', 'school', 'grade']  # Exclude other sensitive fields

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        return super().create(validated_data)

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