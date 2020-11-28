from django.shortcuts import render


def login(request):
	return render(request, 'app/login.html', {})

def home(request):
	return render(request, 'app/home.html', {})

def send(request):
	return render(request, 'app/send.html', {'title':'Send Results'})

def analyze(request):
	return render(request, 'app/analyze.html', {})

def view(request):
	return render(request, 'app/view.html', {})
