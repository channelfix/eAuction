from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import User
import json


def view_profile(request):
    """ View Profile """

    # Check if starts username in query string.
    if 'username' in request.GET:
        # Go to Profile page
        return render(request, 'index.html')
    # Display when it does not start username in query string.
    return HttpResponse('Invalid query string')


def request_profile(request):

    context = {'cars': ['Toyota', 'Lamborghini', 'Porche', 'Ford']}

    # Get all the User objects
    users = User.objects.all()

    # Get the value in query string
    name = request.GET['username']
    print('Name: ', name)

    # Traverse all User objects
    for user in users:
        # Check if the username matches the
        # existing username from User objects.
        if user.username == name:
            return HttpResponse(json.dumps(context))
    # Display when this value does not exist in any User instance.
    return HttpResponse('Not yet registered?')

# Create your views here.
