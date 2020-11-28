from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def login(request):
	return render(request, 'app/login.html', {'title':' - Login','active':'Login'})

def dashboard(request):
	return render(request, 'app/dashboard.html', {'title':' - Dashboard','active':'Dashboard'})

def send(request):
	return render(request, 'app/send.html', {'title':' - Send Results','active':'Send'})

def analyze(request):
	return render(request, 'app/analyze.html', {'title':' - Analyze CT Scan','active':'Analyze'})

def view(request):
	return render(request, 'app/view.html', {'title':' - View Records','active':'View'})

def add(request):
	return render(request, 'app/add.html', {'title':' - Add Patient','active':'Add'})


