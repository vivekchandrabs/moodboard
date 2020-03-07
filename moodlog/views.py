from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from moodlog.models import Mood, MoodLog, Action
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		email = request.POST.get("email")

		user = User.objects.create_user(
				username=username,
				password=password,
				email=email
			)
		login(request, user)

		return redirect("/dashboard/")

	return render(request, "signup.html")

def signin(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user != None:
			login(request, user)
			return redirect("/dashboard/")

	return render(request, "signin.html")

def dashboard(request):
	user = request.user
	moods = Mood.objects.all()
	actions = Action.objects.all()
	moodlog_instances = MoodLog.objects.filter(user=user).order_by('-timestamp')
	return render(request, "dashboard.html", {"moodlog_instances":moodlog_instances, "moods":moods, "actions":actions})

def signout(request):
	logout(request)
	return redirect("/signin/")

def create_moodlog(request):
	if request.method == "POST":
		mood_id = request.POST.get("umood")
		action_id = request.POST.get("uaction")

		mood_instance = Mood.objects.get(pk=mood_id)
		aciton_instance = Action.objects.get(pk=action_id)

		user = request.user
		note = request.POST.get("note")
		
		mood_log = MoodLog.objects.create(
			note = note,
			mood = mood_instance,
			action = aciton_instance,
			user = user		
		)

		return redirect("/dashboard/")