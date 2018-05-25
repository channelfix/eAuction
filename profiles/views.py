from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View
from django.http import HttpResponse


class ProfileView(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)
        user_profile = user.profile
        user_tags = list(user_profile.tags_set.all().values())

        context = {
            'username': user.username,
            'email': user.email,
            'last_name': user.last_name,
            'first_name': user.first_name,
            'biography': user_profile.biography,
            'avatar': user_profile.avatar.url,
            'tags': user_tags,
            'isAuctioneer': user_profile.isAuctioneer
        }

        return JsonResponse(context)


class EditProfile(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)

        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        biography = request.POST.get('biography', '')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.biography = biography
        user_profile = user.profile

        if request.FILES:
            user_profile.avatar = request.FILES['imageFile']

        user_profile.save()
        user.save()

        return HttpResponse('Successfully Changed Profile.')


class EditPassword(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)

        if(user.check_password(request.POST.get('old_password', ''))):
            user.set_password(request.POST.get('new_password', ''))
            user.save()
            return HttpResponse('Changed Password: You will be redirect to the login page.')

        return HttpResponse('Incorrect Old Password')
