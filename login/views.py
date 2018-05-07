import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# @ensure_csrf_cookie
# def index(request):
#     return render(request, 'index.html')


# class LoginView(TemplateView):
#     template_name = 'index.html'


# class IndexView(LoginView):
#     template_name = '../templates/index.html'

#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html')
# @ensure_csrf_cookie
def IndexView(request):
    return render(request, 'index.html', {'isValid': True})

# @ensure_csrf_cookie
# def IndexPost(request):
#     print(request.method)
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         isValid = False

#         if User.objects.filter(username=username,
#                                password=password).exists() is True:
#             isValid = True
#             return HttpResponse(json.dumps({'isValid': isValid}))
#         else:
#             return HttpResponseBadRequest()
    # else:
    #     return HttpResponseBadRequest()


# @method_decorator(csrf_exempt, name='dispatch')
class IndexViewPost(View):
    # @ensure_csrf_cookie
    def post(self, request):
        print(request.method)
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            username = body['username']
            password = body['password']
            isValid = False
            print(username, password)
            user = authenticate(username=username, password=password)

            if user is not None:
                isValid = True
                print("Success")
                return HttpResponse(json.dumps({'isValid': isValid}))
            else:
                print("Access Denied")
                return HttpResponseBadRequest()
