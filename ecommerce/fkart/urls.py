from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_product, name='add_product'),
    path('index/', views.index, name="index"),
]