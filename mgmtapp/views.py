from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
import re

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect("/")
        else:
            messages.error(request, 'User not found!')
            return redirect("/accounts/login")
    return redirect('/accounts/login')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password == confirm_password:
            if not (len(password)>=8):
                messages.error(request, 'Password must contain at least 8 characters.')
                return redirect("/accounts/signup")
            if not re.findall('[0-9]', password):
                messages.error(request, 'Password must contain at least 1 digit(0-9)')
                return redirect("/accounts/signup")
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect("/accounts/signup")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Signed up successfully')
                return redirect("/accounts/login")
        else:
            messages.error(request, 'Passwords do not match')
            return redirect("/accounts/signup")


def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)