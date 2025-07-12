from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skill/', views.skill, name='skill'),
    path('swap_skill/', views.swap_skill, name='swap_skill'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
]