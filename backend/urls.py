  
'''habit URL Configuration'''
from django.urls import path

from . import views

urlpatterns =[
    path('', views.api_overview),
]
