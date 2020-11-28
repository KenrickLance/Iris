from django.urls import path
from . import views

urlpatterns = [
	path('/login', views.login, name='login'),
    path('/home', views.home, name='home'),
    path('/scan', views.scan, name='scan'),
    path('/analyze', views.analyze, name='analyze')
    path('/view/<int:patient_id>', views.view, name='view')
]