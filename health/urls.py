from django.urls import path
from .import views

app_name = 'health'

urlpatterns =[
    path('first/', views.health_first, name='first'),
    path('second/', views.health_second, name='second'),
    path('third/', views.health_third, name='third'),
    path('four/', views.health_four, name='four'),
    path('five/', views.health_five, name='five'),
    path('six/', views.health_six, name='six'),
    path('seven/', views.health_seven, name='seven'),
]