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
        queryset = User.objects.filter(username=user.username)
        user_dict = list(queryset.values('first_name', 'last_name', 'email'))

        # Get the Profile model
        user_profile = user.profile

        # Get the filename for avatar
        pic_name = user_profile.file_name

        # Get the Avatar model
        avatar = user_profile.avatar

        # Get the Biography from a given Profile object
        bio = user_profile.biography

        context = {
            'pic_name': pic_name,
            'avatar': avatar,
            'bio': bio
        }

        # get all the tags for this user instance.
        # tags_dict = list(user.profile.tags_set.all().values())

        # Concatenate all the fields given from
        # User, Profile and Tag above.profile

        # context.update(user_dict[0])
        # context.update(profile_dict)
        # context.update({'tags': tags_dict})

        # print(context)

        return HttpResponse(json.dumps(context))

    return HttpResponse('Failed to login')
