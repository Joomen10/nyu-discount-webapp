from django.shortcuts import render
from django.conf import settings

def signup_view(request):
    context = {
        "signup_api_url": settings.SIGNUP_API_URL  # 환경변수에서 가져옴
    }
    return render(request, "map/signup.html", context)
