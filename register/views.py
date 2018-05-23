import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from profiles.models import Profile
from django.db.utils import IntegrityError
# Create your views here.


class RegisterViewPost(View):
    def post(self, request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(first_name=firstname,
                                            last_name=lastname,
                                            username=username,
                                            email=email,
                                            password=password,)

            newuser = get_object_or_404(User, username=username)
            Profile.objects.create(user=newuser)
        except IntegrityError:
            return HttpResponseBadRequest()

        return HttpResponse(json.dumps({'success': True}))
