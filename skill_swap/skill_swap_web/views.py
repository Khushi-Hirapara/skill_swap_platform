from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')


def skill(request):
    return render(request, 'skill.html')

def swap_skill(request):
    return render(request, 'swap_skill.html')


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import SwapRequest, Skill, Profile
from django import forms

# ✅ Inline Form Class (only if you don't have forms.py)
class SwapRequestForm(forms.ModelForm):
    class Meta:
        model = SwapRequest
        fields = ['offered_skill', 'wanted_skill', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }

# View function using the form
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

