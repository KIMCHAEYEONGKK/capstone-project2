from django.urls import path
from . import views

app_name = 'board'

urlpatterns =[
    path('board_list/', views.board_list, name='board_list'),
    path('board_notice/', views.notice, name='notice'),
    path('board_write/', views.board_write, name='board_write'),
    path('board_delete/<int:pk>', views.board_delete, name='board_delete'),
    path('board_update/<int:pk>', views.board_update, name='board_update'),
]