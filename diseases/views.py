from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context


# Create your views here.
def index(request):
	return render_to_response('diseases/index.html')