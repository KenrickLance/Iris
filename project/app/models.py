import os
import time

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

def make_file_path_name(instance, filename):
	filename, file_extension = os.path.splitext(filename)
	return f'{instance.patient.id}_{instance.patient.lastname}/{instance.patient.lastname}_{instance.test}_{int(time.time())}{file_extension}'

class Patient(models.Model):
	lastname = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	middlename = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	email = models.EmailField()

	def __str__(self):
		return f'{self.lastname}, {self.firstname} {self.middlename}'

class Doctor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	lastname = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	middlename = models.CharField(max_length=100)

	def __str__(self):
		return f'Dr. {self.lastname}, {self.firstname} {self.middlename}'

class Record(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	test = models.CharField(max_length=100)
	file_path = models.FileField(upload_to = make_file_path_name)
	notes = models.TextField()
	result = models.CharField(max_length=100)
	time = models.DateTimeField()

	def __str__(self):
		return f'Patient: {self.patient} | Doctor: {self.doctor} | {self.time}'

