from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import override
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import Users, Restaurants, Menus, Discounts, Reviews
from .serializers import (
    UsersSerializer,
    RestaurantsSerializer,
    MenusSerializer,
    DiscountsSerializer,
    ReviewsSerializer,
)

# ✅ Secure User Registration
def register_view(request):
    with override("en"):  # 영어
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            school = request.POST.get("school")
            grade = request.POST.get("grade")

            # Ensure email is unique
            if Users.objects.filter(email=email).exists():
                return render(request, "restaurant/dj_register.html", {"error": "Email already exists."})

            # Hash password before saving
            hashed_password = make_password(password)

            # Create user
            user = Users.objects.create(
                name=name, email=email, password=hashed_password, school=school, grade=grade
            )

            return redirect("/restaurant/login/")  # Redirect to login page after signup

        return render(request, "restaurant/dj_register.html")

# ✅ Secure User Login API
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Check hashed password
        if not check_password(password, user.password):
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate or retrieve authentication token
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "message": "Login successful!"
        }, status=status.HTTP_200_OK)

# ✅ Secure Logout API
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # ✅ Deletes the token
        return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)

# ✅ User API Views
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