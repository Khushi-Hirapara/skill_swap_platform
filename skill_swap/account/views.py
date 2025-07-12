from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': CustomUserCreationForm()})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'form': form, 'error': 'Username already exists'})
        else:
            return render(request, 'signup.html', {'form': form, 'error': 'Invalid data'})

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Invalid credentials'})
        else:
            login(request, user)
            return redirect('home')

def logoutaccount(request):
    logout(request)
    return redirect('home')
