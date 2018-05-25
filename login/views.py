from django.http import JsonResponse
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.generic import View
from django.contrib import auth


class IndexViewPost(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return JsonResponse({'isValid': True})
        else:
            return HttpResponseBadRequest()


class LogoutOutUser(View):
    def post(self, request):
        print(request)
        auth.logout(request)
        return HttpResponse("Success")
