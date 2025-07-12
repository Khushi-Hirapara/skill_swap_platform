from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('skill/', views.skill, name='skill'),
    path('skill/', views.skill, name='skill'),
    path('swap_skill/', views.swap_skill, name='swap_skill'),]