from django.urls import path
from . import views


urlpatterns = [
    path('request_profile/', views.request_profile),
    path('sign_in/', views.view_profile),
    path('sample/', views.SampleCase.as_view()),
]
