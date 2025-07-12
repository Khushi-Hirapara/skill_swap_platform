from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


# def login_view(request):
#     return render(request, 'registration/login.html')

# def signup_view(request):
#     return render(request,'registration/signup.html')

def profile(request):
    return render(request, 'profile.html')


def skill(request):
    return render(request, 'skill.html')

def swap_skill(request):
    return render(request, 'swap_skill.html')

