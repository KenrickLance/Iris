from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


from .forms import LoginForm

def login(request):
	if request.user.is_authenticated:
		return render(request, 'app/home.html')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login_auth(request, user)
			return redirect('/home')
		else:
			form = AuthenticationForm(request.POST)
			return render(request, 'app/login.html', {'form': form})
	else:
		form = AuthenticationForm()
		return render(request, 'app/login.html', {'form': form})

def dashboard(request):
	return render(request, 'app/dashboard.html', {'title':' - Dashboard','active':'Dashboard'})
	
def logout(request):
	logout_auth(request)
	return redirect('/login')

@login_required
def home(request):
	return render(request, 'app/home.html', {})

def send(request):
	return render(request, 'app/send.html', {'title':' - Send Results','active':'Send'})

def analyze(request):
	return render(request, 'app/analyze.html', {'title':' - Analyze CT Scan','active':'Analyze'})

def view(request):
	return render(request, 'app/view.html', {'title':' - View Records','active':'View'})

def add(request):
	return render(request, 'app/add.html', {'title':' - Add Patient','active':'Add'})


