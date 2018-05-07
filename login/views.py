import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# @ensure_csrf_cookie
# def index(request):
#     return render(request, 'index.html')


# class LoginView(TemplateView):
#     template_name = 'index.html'


class IndexView(LoginView):
    template_name = '../templates/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def IndexPost(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        isValid = False

        if User.objects.filter(username) is True and User.objects.filter(password) is True:
            isValid = True
            return HttpResponse(json.dumps({'isValid': isValid}))
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()

        """
# class IndexViewPost(View):
    # @ensure_csrf_cookie
    # def post(self, request, *args, **kwargs):
    #     user = authenticate(username=request.POST.get('username'),
    #                         password=request.POST.get('password'))
    #     if user is not None:
    #         isValid = True
    #         context = {
    #             'isValid': isValid
    #         }
    #     else:
    #         return HttpResponseBadRequest()

    #     return HttpResponse(json.dumps(context))
        """
