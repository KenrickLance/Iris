from django import forms
from .models import Patient, Doctor, Record

class AddPatientForm(forms.Form):
    lastname = forms.CharField(label='Last name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    firstname = forms.CharField(label='First name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    middlename = forms.CharField(label='Middle name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Middle name'}))
    phone = forms.CharField(label='Phone', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    email = forms.EmailField(label='Email address', widget=forms.TextInput(attrs={'placeholder': 'Email address'}))

class SendResultsForm(forms.Form):
	patient = forms.ModelChoiceField(label='Patient name', queryset=Patient.objects.all(), required=True, empty_label='Patient name', widget=forms.Select(attrs={'class': 'ui search dropdown'}))
	doctor = forms.ModelChoiceField(label='Assigned doctor', queryset=Doctor.objects.all(), required=True, empty_label='Assigned doctor', widget=forms.Select(attrs={'class': 'ui search dropdown'}))
	test = forms.CharField(label='Test type', max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Test type'}))
	result = forms.CharField(label='Result', max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Result'}))
	file = forms.FileField(label='Upload file')
	notes =  forms.CharField(label='Notes', widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		user_id = kwargs.pop('user_id', None)
		print(user_id)
		super(SendResultsForm, self).__init__(*args, **kwargs)
		if user_id:
			self.fields['doctor'].queryset = Doctor.objects.filter(user=user_id)
