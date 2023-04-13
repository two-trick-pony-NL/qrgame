from django.contrib import admin
from django.urls import path, include
from qrcodegame import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('test', views.test, name='homepage'),
    path('random', views.random, name='random'),
]