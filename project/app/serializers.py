from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Patient, Doctor, Record

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'lastname', 'firstname', 'middlename', 'phone', 'email')

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'patient', 'doctor', 'test', 'file_path', 'notes', 'result', 'time')

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'user', 'lastname', 'firstname', 'middlename')