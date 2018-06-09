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
            isAuctioneer = user.profile.isAuctioneer
            credits = user.profile.total_credits

            return JsonResponse({'isValid': True,
                                 'isAuctioneer': isAuctioneer,
                                 'credits': credits})
        else:
            return HttpResponseBadRequest()


class LogoutUser(View):
    def post(self, request):
        auth.logout(request)
        return HttpResponse("Success")
