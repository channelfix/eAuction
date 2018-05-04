from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'login'
urlpatterns = [
	# path('', views.index, name='index'),
	path('', views.index, name='login-page'),
	path('test/', views.test),
]