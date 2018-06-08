import json
from profiles.models import Profile
from django.http import HttpResponse
from django.views.generic import View
from django.db.models import Q


class BrowseView(View):
    def post(self, request):
        print(request.POST)
        query_name = request.POST.get('browseQuery', None)
        query_filter = request.POST.get('browseFilter', None)
        query_set = Profile.objects.all()

        print(query_name)
        print(query_filter)
        if query_filter and not query_name:
            print("not query_filter and query_name")
            query_set = query_set.filter(
                tags__name__contains=query_filter).distinct()
        elif not query_filter and query_name:
            print("query_filter and not query_name")
            query_set = query_set.filter(
                Q(user__first_name__contains=query_name) |
                Q(user__last_name__contains=query_name)).distinct()
        else:
            print("all")
            query_set = query_set.filter(
                Q(user__first_name__contains=query_name) |
                Q(user__last_name__contains=query_name),
                tags__name__contains=query_filter).distinct()

        context = []
        for obj in query_set:
            tags = list(obj.tags_set.values_list('name', flat=True))
            context.append({
                'pk': obj.user.pk,
                'username': obj.user.username,
                'last_name': obj.user.last_name,
                'first_name': obj.user.first_name,
                'description': obj.biography,
                'contact_number': obj.contact_number,
                'isAuctioneer': obj.isAuctioneer,
                'tags': tags,
            })

        return HttpResponse(json.dumps(context))
