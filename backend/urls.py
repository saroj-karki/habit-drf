  
'''habit URL Configuration'''
from django.urls import path

from . import views

urlpatterns =[
    path('habits/', views.habits),
    path('habit/<int:primary_key>/', views.habit_details),
]
