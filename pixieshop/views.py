from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'shop/index.html')

def about(request):
	"""
	docstring
	"""
	return HttpResponse("about page")

def contact(request):
	"""
	docstring
	"""
	return HttpResponse("contact page")

def tracker(request):
	"""
	docstring
	"""
	return HttpResponse("tracker page")

def search(request):
	"""
	docstring
	"""
	return HttpResponse("search page")

def prodView(request):
	"""
	docstring
	"""
	return HttpResponse("prodView page")

def checkout(request):
	"""
	docstring
	"""
	return HttpResponse("checkout page")
