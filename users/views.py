from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.utils.translation import override

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("restaurant:home")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})

def register_view(request):
    with override("en"):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("users:login")
        else:
            form = UserCreationForm()
        return render(request, "users/register.html", {"form": form})
    
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")