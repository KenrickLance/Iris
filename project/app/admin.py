from django.contrib import admin
from .models import Hospital, Patient, Doctor, Record

admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Record)
