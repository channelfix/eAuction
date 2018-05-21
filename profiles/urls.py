from django.urls import path
from . import views


urlpatterns = [
    path('request_profile_details/', views.request_profile_details),
    path('save_profile_pic/', views.save_profile_pic),
]
