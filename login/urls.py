from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'login'
urlpatterns = [
	# path('', views.index, name='index'),
	path('', views.LoginView.as_view(), name='login-page')
]