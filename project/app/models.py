from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

def make_file_path_name(instance, filename):
	return f'patient{instance.patient.id}/{filename}'

class Patient(models.Model):
	lastname = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	middlename = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	email = models.EmailField()

class Doctor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	lastname = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	middlename = models.CharField(max_length=100)

class Record(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	test = models.CharField(max_length=100)
	file_path = models.FileField(upload_to = make_file_path_name)
	notes = models.TextField()
	result = models.CharField(max_length=100)
	time = models.DateTimeField()


