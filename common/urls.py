from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from common.views import signup, login, logout


app_name = 'common'

urlpatterns =[
    path('signup/',views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="common/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('health_page/', views.health, name="health")

]