from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mood(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    emoji = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} | {self.emoji}"


class Action(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    emoji = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} | {self.emoji}"


class MoodLog(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True)
    action = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True)
    note = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.mood} | {self.timestamp}"