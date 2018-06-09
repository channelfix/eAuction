from django.urls import path
from . import views


urlpatterns = [
    path('request_profile_details/', views.ProfileView.as_view()),
    path('edit_profile_details/', views.EditProfile.as_view()),
    path('edit_password/', views.EditPassword.as_view()),
    path('remove_tag/', views.TagRemoval.as_view()),
    path('subscribe/', views.Subscribe.as_view())
]
