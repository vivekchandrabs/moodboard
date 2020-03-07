from django.contrib import admin

from moodlog.models import Mood, Action, MoodLog

# Register your models here.

admin.site.register([Mood, Action, MoodLog])
