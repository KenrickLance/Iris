from django import forms

class AddPatientForm(forms.Form):
    lastname = forms.CharField(label='Last name', max_length=100)
    firstname = forms.CharField(label='First name', max_length=100)
    middlename = forms.CharField(label='Middle name', max_length=100)
    phone = forms.CharField(label='Middle name', max_length=20)
    email = forms.EmailField(label='Email Address')