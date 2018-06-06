from profiles.models import Profile
from django.http import HttpResponse
from django.views.generic import View
from django.core import serializers
from django.db.models import Q


class BrowseView(View):
    def get(self, request):
        print(request.GET)
        query_name = request.GET.get('queryName', '')
        query_filter = request.GET.get('queryFilter', '')
        query_set = Profile.objects.filter(
            Q(user__first_name__contains=query_name) |
            Q(user__last_name__contains=query_name) |
            Q(tags__name__contains=query_filter)).distinct()
        print(query_set)
        query_set_json = serializers.serialize('json', query_set)
        return HttpResponse(query_set_json, content_type='application/json')
