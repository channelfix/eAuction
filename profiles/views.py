from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View
from django.http import HttpResponse
from tags.models import Tags
from profiles.models import Subscribed, Credit
from django.db.models import Sum


class ProfileView(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)
        user_profile = user.profile
        user_tags = list(user_profile.tags_set.all().values('name'))

        hasSubscribed = Subscribed.objects.filter(auctioneer=user,
                                                  bidder=request.user).exists()
        context = {
            'username': user.username,
            'email': user.email,
            'last_name': user.last_name,
            'first_name': user.first_name,
            'biography': user_profile.biography,
            'avatar': user_profile.avatar.url,
            'tags': user_tags,
            'isAuctioneer': user_profile.isAuctioneer,
            'subscribers': user_profile.countSubscribers,
            'hasSubscribed': hasSubscribed,
            'contact_number': user.profile.contact_number,
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
        list_of_tags = request.POST.get('tags', '')
        contact_number = request.POST.get('contact_number', '')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.profile.biography = biography
        user.profile.contact_number = contact_number
        user_profile = user.profile

        if request.FILES:
            user_profile.avatar = request.FILES['imageFile']

        user_profile.save()
        user.save()

        if list_of_tags != '':
            tags = list_of_tags.split(',')
            for tag in tags:
                t, created = Tags.objects.get_or_create(name=tag)
                user_profile.tags_set.add(t)

        return HttpResponse('Successfully Changed Profile.')


class EditPassword(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)

        if(user.check_password(request.POST.get('old_password', ''))):
            user.set_password(request.POST.get('new_password', ''))
            user.save()
            return HttpResponse('Changed Password: You will be redirect to'
                                ' the login page.')

        return HttpResponse('Incorrect Old Password')


class TagRemoval(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)
        sent_tag = request.POST.get('tag', '')
        tag = Tags.objects.filter(name=sent_tag)

        if tag.exists():
            tag = user.profile.tags_set.get(name=sent_tag)
            tag.delete()
            return HttpResponse('Removed tag successfully')
        return HttpResponse('%s not found' % sent_tag)


class Subscribe(View):
    def post(self, request):
        current_user = request.user
        sent_username = request.POST.get('username', '')
        subscribed_user = User.objects.get(username=sent_username)

        subscribed = Subscribed.objects.filter(auctioneer=subscribed_user,
                                               bidder=current_user)

        if subscribed:
            subscribed.delete()
            res = 'Subscribe'
        else:
            Subscribed.objects.create(auctioneer=subscribed_user,
                                      bidder=current_user)
            res = 'Unsubscribe'
            subscribed_user.profile.save()

        return HttpResponse(res)


class UpdateCredits(View):
    def post(self, request):
        current_user = request.user
        amount = request.POST.get('amount', '')
        credit = Credit.objects.create(credit_amount=amount,
                                       profile=current_user.profile)
        total_credit = Credit.objects.filter(
            profile=current_user.profile
        ).aggregate(Sum('credit_amount'))

        print(total_credit)

        return JsonResponse({'total_credit': total_credit})
