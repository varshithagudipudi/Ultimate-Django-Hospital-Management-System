from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

def home(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, "Account created successfully ✅")
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Welcome back 👋")
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect("login")
