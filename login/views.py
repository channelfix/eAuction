from django.http import JsonResponse
from django.http import HttpResponseBadRequest
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
