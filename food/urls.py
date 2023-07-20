from django.urls import path
from .import views

app_name = 'food'

urlpatterns =[
    path('food/', views.request_Calorie, name='food'),
    path('food_menu/', views.food, name='food_menu')
]