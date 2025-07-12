from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Skill, SwapRequest
from .forms import SwapRequestForm

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def skill(request):
    return render(request, 'skill.html')

def swap_skill(request):
    return render(request, 'swap_skill.html')

@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)

    if request.method == 'POST':
        form = SwapRequestForm(request.POST)
        if form.is_valid():
            swap_request = form.save(commit=False)
            swap_request.from_user = request.user
            swap_request.to_user = user_profile.user
            swap_request.save()
            return redirect('profile', username=username)
    else:
        form = SwapRequestForm()

    context = {
        'profile': user_profile,
        'form': form,
    }
    return render(request, 'skill.html', context)

def swap_skill(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'swap_skill.html', {'profile': profile})

def skill_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'skill_detail.html', {'profile': profile})




