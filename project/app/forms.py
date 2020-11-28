from django import forms
from django.forms.widgets import Textarea
from .models import Patient, Doctor, Record

class AddPatientForm(forms.Form):
    lastname = forms.CharField(label='Last name', max_length=100, required=True)
    firstname = forms.CharField(label='First name', max_length=100, required=True)
    middlename = forms.CharField(label='Middle name', max_length=100, required=True)
    phone = forms.CharField(label='Phone', max_length=20)
    email = forms.EmailField(label='Email Address')

class SendResultsForm(forms.Form):
	patient = forms.ModelChoiceField(label='Patient Name', queryset=Patient.objects.all(), required=True)
	doctor = forms.ModelChoiceField(label='Assigned Doctor', queryset=Doctor.objects.all(), required=True)
	test = forms.CharField(label='Test Type', max_length=20, required=True)
	result = forms.CharField(label='Result', max_length=20, required=True)
	file = forms.FileField(label='Upload File')
	notes =  forms.CharField(label='Doctor\'s Notes', widget=Textarea)