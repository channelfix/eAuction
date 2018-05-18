from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
import json


def view_profile(request):

    # Check if the username and password were filled.
    if 'username' in request.GET and 'password' in request.GET:
        username = request.POST.get('username', request.GET['username'])
        password = request.POST.get('password', request.GET['password'])

        user = auth.authenticate(username=username, password=password)

        # Check if th user account is still active.
        if user and user.is_active:
            # Store the username and password temporarily
            # to be used by request_profile function.
            auth.login(request, user)
            # Go to Profile page.
            return render(request, 'index.html')
        else:
            return HttpResponse('Failed to Login')

    return HttpResponse('404 Not Found')


def request_profile(request):

    user = request.user

    # Get the Profile object
    user_profile = user.profile

    # Get the list of tags
    user_tags = list(user_profile.tags_set.all().values())

    # Send all current User details to Client.
    context = {
        'username': user.username,
        'email': user.email,
        'last_name': user.last_name,
        'first_name': user.first_name,
        'filename': user_profile.file_name,
        'biography': user_profile.biography,
        'avatar': user_profile.avatar.url,
        'tags': user_tags
    }

    return HttpResponse(json.dumps(context))
