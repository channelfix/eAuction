import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View
from django.contrib.auth.models import User
# Create your views here.


class RegisterViewPost(View):
    def post(self, request):
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name=firstname,
                                        last_name=lastname,
                                        username=username,
                                        email=email,
                                        password=password,
                                        is_staff=False,
                                        is_admin=False)

        if user.username_validator() is True and User.objects.get(username=username).exists() is False:
            return HttpResponse(json.dumps({'success': True}))
        else:
            return HttpResponseBadRequest()
