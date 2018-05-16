from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from profiles.models import Profile
import json


def view_profile(request):

    if 'username' in request.GET and 'password' in request.GET:
        username = request.POST.get('username', request.GET['username'])
        password = request.POST.get('password', request.GET['password'])

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('Failed to Login')

    return HttpResponse('404 Not Found')


def request_profile(request):

    user = request.user
    if user and user.is_active:
        # get the name, email from given User model.
        user = User.objects.get(username=user.username)
        user_profile = user.profile
        user_tags = list(user_profile.tags_set.all().values())
        print(user_profile.avatar.url)

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

    return HttpResponse('Failed to login')
