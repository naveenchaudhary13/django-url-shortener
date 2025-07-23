# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View


class LoginView(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")
        else:
            messages.error(request, "Invalid credentials!")
        return redirect("home")


class SignupView(View):
    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("home")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("home")

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, "Signup successful!")
        return redirect("home")


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logout successful!")
        return redirect("home")
