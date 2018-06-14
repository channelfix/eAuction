from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View
from django.http import HttpResponse
from profiles.models import Subscribed, Credit, Tags
from django.db.models import Sum


class ProfileView(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)
        user_profile = user.profile
        user_tags = list(user_profile.tags_set.all().values('name'))

        hasSubscribed = Subscribed.objects.filter(auctioneer=user,
                                                  bidder=request.user).exists()
        phone_number = user.profile.phone_number
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
            'hasSubscribed': hasSubscribed            
        }

        if phone_number != '':
            context['contact_number'] = '+'+str(phone_number.country_code)+str(phone_number.national_number)

        return JsonResponse(context)


class EditProfile(View):
    def post(self, request):
        sent_username = request.POST.get('username', '')
        user = User.objects.get(username=sent_username)

        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        biography = request.POST.get('biography', '')        
        contact_number = request.POST.get('contact_number', '')
        print(contact_number)


        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.profile.biography = biography
        user.profile.phone_number = contact_number
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


class TagListView(View):
    def get(self, request):
        tag_list = list(Tags.objects.all().values('name').distinct())

        return JsonResponse({'tags': tag_list})


class ProductCreatedView(View):
    def post(self, request):
        user = request.user
        product_name = request.POST.get('name', '')        
        product_tag = request.POST.get('tag','')

        user_profile = user.profile

        # Set a new tag, if it does not exist on this profile.
        tag, created = user_profile.tags_set.get_or_create(name=product_tag)
        tag.products.create(name=product_name)


        return HttpResponse('Product created')


class RetrieveProductView(View):
    def get(self, request):
        # product name, tag and date sold
        user_profile = request.user.profile
        product_list = list(user_profile.tags_set.all().values('products__name',
                                                               'name','products__date_sold')
                                                       .order_by('name'))

        return JsonResponse({'products': product_list})        


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

        return JsonResponse({'total_credit': total_credit})
