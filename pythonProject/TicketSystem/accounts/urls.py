from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('register', views.register, name='register'),
]