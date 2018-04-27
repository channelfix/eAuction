import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def index(request):
	name = request.POST.get('name')
	context = {
		'name': name
	}
	# return HttpResponse(json.dumps(context))
	return render(request, 'auction/index.html', context)