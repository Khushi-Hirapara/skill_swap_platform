from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_view, name='login'),
    # path('signup/',views.signup_view, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('skill/', views.skill, name='skill'),
    path('swap_skill/', views.swap_skill, name='swap_skill'),

]
