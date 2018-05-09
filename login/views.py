import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate


class IndexView(LoginView):
    template_name = '../templates/index.html'

    # def post(self, request, *args, **kwargs):
    #     return render(request, 'index.html')


class IndexViewPost(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        print(request.POST)

        if user is not None:
            print("Success")
            return HttpResponse(json.dumps({'isValid': True}))
        else:
            print("Access Denied")
            return HttpResponseBadRequest()
