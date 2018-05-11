import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate


class IndexViewPost(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user is not None:
            return HttpResponse(json.dumps({'isValid': True}))
        else:
            return HttpResponseBadRequest()
