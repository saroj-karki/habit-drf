  
'''habit URL Configuration'''
from django.urls import path

from . import views

urlpatterns =[
    path('habits/', views.habits),
    path('habit/<int:primary_key>/', views.habit_details),
    path('habit-create/', views.habit_create),
    path('habit-update/<int:primary_key>/', views.habit_update),
    path('habit-delete/<int:primary_key>/', views.habit_delete),
    path('habit-items/', views.daily_habit_items),
    path('habit-item-create/', views.habit_item_create),
]
