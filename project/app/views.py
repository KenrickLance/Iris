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


from .models import Patient, Doctor, Record
from .forms import AddPatientForm

def login(request):
	if request.user.is_authenticated:
		return render(request, 'app/dashboard.html')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login_auth(request, user)
			return redirect('/dashboard')
		else:
			form = AuthenticationForm(request.POST)
			return render(request, 'app/login.html', {'form': form})
	else:
		form = AuthenticationForm()
		return render(request, 'app/login.html', {'form': form})

def logout(request):
	logout_auth(request)
	return redirect('/login')

@login_required
def dashboard(request):
	return render(request, 'app/dashboard.html', {'title':' - Dashboard', 'active':'Dashboard'})

@login_required
def send(request):
	return render(request, 'app/send.html', {'title':' - Send Results', 'active':'Send'})

@login_required
def analyze(request):
	return render(request, 'app/analyze.html', {'title':' - Analyze CT Scan', 'active':'Analyze'})

@login_required
def view(request):
	return render(request, 'app/view.html', {'title':' - View Records', 'active':'View'})

@login_required
def add(request):
	if request.method =='POST':
		form = AddPatientForm(request.POST)
		if form.is_valid():
			lastname = request.POST['lastname']
			firstname = request.POST['firstname']
			middlename = request.POST['middlename']
			phone = request.POST['phone']
			email = request.POST['email']
			new_patient = Patient(lastname=lastname, firstname=firstname, middlename=middlename, phone=phone, email=email)
			new_patient.save()
			return HttpResponseRedirect('/send')
	else:
		form = AddPatientForm()

	return render(request, 'app/add.html', {'title':' - Add Patient', 'active':'Add', 'form':form})


