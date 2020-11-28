from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'view/patient', views.api_view_patient, basename='patient')
router.register(r'view/doctor', views.api_view_doctor, basename='doctor')
router.register(r'view/record', views.api_view_record, basename='record')
router.register(r'user', views.api_user, basename='user')

urlpatterns = [
	path('login', views.login, name='login'),
    path('send', views.send, name='send'),
    path('analyze', views.analyze, name='analyze'),
    path('view', views.view, name='view'),
    path('add', views.add, name='add'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('download', views.download, name='download'),
    path('get_file', views.get_file, name='get_file')

    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/login', views.api_login.as_view(), name='api_login'),
]