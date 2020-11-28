from django.utils import timezone
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
from django.conf import settings

from .models import Patient, Doctor, Record
from .forms import AddPatientForm, SendResultsForm

from .functions import send_sms, send_email, generate_pdf_password, encrypt_pdf

from django.contrib.auth.models import User

from rest_framework import viewsets, generics
from rest_framework.response import Response as RestResponse
from rest_framework.views import APIView
from .serializers import PatientSerializer, DoctorSerializer, RecordSerializer, UserSerializer


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
	if request.method == 'POST':
		form = SendResultsForm(request.POST, request.FILES, user_id=request.user.id)
		print(form.is_valid())
		print(form.errors)
		if form.is_valid():
			patient_id = request.POST['patient']
			patient = Patient.objects.get(pk=patient_id)
			doctor_id = request.POST['doctor']
			doctor = Doctor.objects.get(pk=doctor_id)
			test = request.POST['test']
			result = request.POST['result']
			file = request.FILES['file']
			notes = request.POST['notes']
			time = timezone.now()
			new_record = Record(patient=patient, doctor=doctor, test=test, result=result, file_path=file, notes=notes, time=time)
			new_record.save()
			absolute_file_path = f'{settings.BASE_DIR}{settings.MEDIA_URL}{new_record.file_path}'
			print(absolute_file_path)
			encrypt_pdf(absolute_file_path, '1234')

			return HttpResponseRedirect('/view')
	else:
		print(request.user.id)
		form = SendResultsForm(user_id=request.user.id)
	print(settings.BASE_DIR)
	return render(request, 'app/send.html', {'title':' - Send Results', 'active':'Send', 'form':form})

@login_required
def analyze(request):
	return render(request, 'app/analyze.html', {'title':' - Analyze CT Scan', 'active':'Analyze'})

@login_required
def view(request):
	print(request.user.id)
	doctors = Doctor.objects.filter(user__id=request.user.id)
	doctor_pks = list(doctors.values_list('id', flat=True).distinct())
	records = Record.objects.filter(doctor__in=doctor_pks)
	patient_pks = list(records.values_list('patient__id', flat=True).distinct())
	patients = Patient.objects.filter(id__in=patient_pks)
	return render(request, 'app/view.html', {'title':' - View Records', 'active':'View', 'doctors':doctors, 'records':records, 'patients':patients})

@login_required
def add(request):
	if request.method =='POST':
		form = AddPatientForm(request.POST)
		if form.is_valid():
			lastname = request.POST['lastname']
			print(lastname)
			firstname = request.POST['firstname']
			middlename = request.POST['middlename']
			phone = request.POST['phone']
			email = request.POST['email']
			print(request.POST)
			new_patient = Patient(lastname=lastname, firstname=firstname, middlename=middlename, phone=phone, email=email)
			new_patient.save()
			return HttpResponseRedirect('/send')
	else:
		form = AddPatientForm()

	return render(request, 'app/add.html', {'title':' - Add Patient', 'active':'Add', 'form':form})

class api_view_patient(viewsets.ModelViewSet):
	def get_queryset(self):
		user_id = self.request.query_params.get('user_id', None)
		if user_id == None:
			return Patient.objects.all()
		doctors = Doctor.objects.filter(user__id=user_id)
		doctor_pks = list(doctors.values_list('id', flat=True).distinct())
		records = Record.objects.filter(doctor__in=doctor_pks)
		patient_pks = list(records.values_list('patient__id', flat=True).distinct())
		patients = Patient.objects.filter(id__in=patient_pks)
		return patients
	serializer_class = PatientSerializer

class api_view_doctor(viewsets.ModelViewSet):
	def get_queryset(self):
		user_id = self.request.query_params.get('user_id', None)
		if user_id == None:
			return Doctor.objects.all()
		doctors = Doctor.objects.filter(user__id=user_id)
		return doctors
	serializer_class = DoctorSerializer

class api_view_record(viewsets.ModelViewSet):
	def get_queryset(self):
		user_id = self.request.query_params.get('user_id', None)
		if user_id == None:
			return Record.objects.all()
		doctors = Doctor.objects.filter(user__id=user_id)
		doctor_pks = list(doctors.values_list('id', flat=True).distinct())
		records = Record.objects.filter(doctor__in=doctor_pks)
		return records
	serializer_class = RecordSerializer

class api_user(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class api_login(APIView):
	def post(self, request, format=None):
		username = request.data.get('username', None)
		password = request.data.get('password', None)
		user = authenticate(username=username, password=password)
		if user:
			authenticated = 1
			user_id = user.id
		else:
			authenticated = 0
			user_id = None
		out = {'authenticated': authenticated, 'user_id': user_id}
		return RestResponse(out)