from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse


def request_profile_details(request):
    sent_username = request.POST.get('username', '')

    user = User.objects.get(username=sent_username)

    # Get the Profile object
    user_profile = user.profile

    # Get the list of tags
    user_tags = list(user_profile.tags_set.all().values())

    print(user_profile.avatar.url)

    # Send all current User details to Client.
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


def save_profile_pic(request):
    """ Save Image inside the media folder """

    # File name of the current image to be upload.
    user = request.user
    profile = user.profile
    profile.avatar = request.FILES['imageFile']
    profile.save()

    return HttpResponse('Successfully change profile')
