import day as day
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .forms import LoginForm


def signup(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            tall = form.cleaned_data.get('tall')
            gender = form.cleaned_data.get('gender')
            exercise = form.cleaned_data.get('exercise')

            user = authenticate(username=username, password=password1,name=name,
                                age=age, exercise=exercise, tall=tall,gender=gender)

            login(request,user)
            return redirect('/')
        else:
            return render(request, 'common/signup.html')
    else:
        form = UserCreateForm()

    return render(request, 'common/signup.html', {'form': form})


def view_login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'common/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'common/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('/')
    return render(request, 'common/logout.html')


def home(request):
    return render(request, 'common/home.html')


def index():
    return None
