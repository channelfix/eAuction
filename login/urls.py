from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'login'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='login-page'),
    path('accounts/', views.IndexViewPost.as_view(), name='login-post'),
]