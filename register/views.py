import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from profiles.models import Profile
from django.db.utils import IntegrityError
from django.core.files.images import ImageFile


class RegisterViewPost(View):
    def post(self, request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(first_name=firstname,
                                            last_name=lastname,
                                            username=username,
                                            email=email,
                                            password=password)

            newuser = get_object_or_404(User, username=username)
            profile = Profile.objects.create(user=newuser)
            profile.avatar.save('anonymous.jpg',
                                ImageFile(open('media/anonymous.jpg', 'rb')))
        except IntegrityError:
            return HttpResponseBadRequest()
        profile.save()
        user.save()

        return HttpResponse(json.dumps({'success': True}))
