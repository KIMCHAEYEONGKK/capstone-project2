from django.urls import path
from .import views

app_name = 'setting'

urlpatterns =[
    path('inbody/', views.inbody, name='inbody'),
    # path('inbody_update/', views.inbody_update, name='inbody_update'),
    path('inbody_list/', views.inbody_list, name='inbody_list'),
]