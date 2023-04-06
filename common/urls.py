from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from common.views import signup, login, logout
from .import views


app_name = 'common'

urlpatterns =[
    path('signup/', views.signup, name='signup'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home')
]