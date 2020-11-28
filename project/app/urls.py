from django.urls import path
from . import views

urlpatterns = [
	path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('send', views.send, name='send'),
    path('analyze', views.analyze, name='analyze'),
    path('view', views.view, name='view')
]