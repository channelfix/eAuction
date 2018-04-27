import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView


def index(request):
	return render(request, 'index.html')

# def test(request):
# 	name = request.GET.get('name')
# 	password = request.GET.get('password')
	
# 	isValid = False	

# 	if(name == "bojoluis" and password == "1234"):
# 		isValid = True

# 	context = {
# 		'isValid': isValid,
# 	}

# 	return HttpResponse(json.dumps(context))
	

class LoginView(TemplateView):
	template_name='index.html'