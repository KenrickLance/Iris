from django.urls import path
from . import views

urlpatterns = [
	path('login', views.login, name='login'),
    path('send', views.send, name='send'),
    path('analyze', views.analyze, name='analyze'),
    path('view', views.view, name='view'),
    path('add', views.add, name='add'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout')
]