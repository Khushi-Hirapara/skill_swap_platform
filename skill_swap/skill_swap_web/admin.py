from django.contrib import admin
from .models import Skill, Profile, SwapRequest

# Register your models to show up in Django admin
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(SwapRequest)