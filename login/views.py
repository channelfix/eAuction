import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate


class IndexView(LoginView):
    template_name = '../templates/index.html'

    def post(self, request, *args, **kwargs):
        return render(request, 'index.html')


class IndexViewPost(View):
    # @ensure_csrf_cookie
    def post(self, request):
        print(request.method)
        username = request.POST.get('username', '')
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        isValid = False
        user = authenticate(username=username, password=password)

        if user is not None:
            isValid = True
            print("Success")
            return HttpResponse(json.dumps({'isValid': isValid}))
        else:
            print("Access Denied")
            return HttpResponseBadRequest()
