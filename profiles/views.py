from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View


class ProfileView(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.filter(username=sent_username).first()
        user_profile = user.profile
        user_tags = list(user_profile.tags_set.all().values())

        context = {
            'username': user.username,
            'email': user.email,
            'last_name': user.last_name,
            'first_name': user.first_name,
            'biography': user_profile.biography,
            'avatar': user_profile.avatar.url,
            'tags': user_tags
        }

        return JsonResponse(context)


class EditProfile(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.filter(username=sent_username).first()

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.profile.biography = request.POST.get('biography')
