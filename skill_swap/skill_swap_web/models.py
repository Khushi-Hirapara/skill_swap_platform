from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills_offered = models.ManyToManyField(Skill, related_name='offered_by')
    skills_wanted = models.ManyToManyField(Skill, related_name='wanted_by')
    rating = models.FloatField(default=0.0)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class SwapRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    offered_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='offered_requests')
    wanted_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='wanted_requests')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} ➝ {self.to_user}"



