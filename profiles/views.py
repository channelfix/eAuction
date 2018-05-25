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

        print(context)

        return JsonResponse(context)


class EditProfile(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)

        old_password = request.POST.get('old_password', '')

        if(user.check_password(old_password)):
            new_password = request.POST.get('new_password', '')
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email = request.POST.get('email', '')
            biography = request.POST.get('biography', '')

            user.set_password(new_password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.biography = biography
            user_profile = user.profile
            user_profile.avatar = request.FILES['imageFile']
            user_profile.save()
            user.save()

            return HttpResponse('Successfully Changed Profile.')

        return HttpResponse('Incorrect Old Password')


class SaveImage(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)
        profile = user.profile
        profile.avatar = request.FILES['imageFile']
        profile.save()

        return HttpResponse('Successfully saved image')
