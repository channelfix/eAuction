from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.views.generic import View
from django.contrib.auth import authenticate


class IndexViewPost(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse({'isValid': True})
        else:
            return HttpResponseBadRequest()
