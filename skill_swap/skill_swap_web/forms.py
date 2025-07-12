from django import forms
from .models import SwapRequest

class SwapRequestForm(forms.ModelForm):
    class Meta:
        model = SwapRequest
        fields = ['offered_skill', 'wanted_skill', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }
