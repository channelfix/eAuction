from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.IndexViewPost.as_view(), name='login-post'),
    path('logout/', views.LogoutOutUser.as_view(), name='logout-post')
]
