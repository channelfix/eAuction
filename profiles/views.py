from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
import json
from django.core import serializers


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
        user_profile = user.profile
        user_tags = user_profile.tags_set.all()

        serializer = serializers.serialize('json', [user, user_profile, user_tags])

        # context = {
        #     'user': user,
        #     'user_profile': user_profile,
        #     'user_tags': user_tags
        # }

        return HttpResponse(json.dumps(serializer))

    return HttpResponse('Failed to login')
