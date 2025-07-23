from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader



def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

def contact(request):
  return render(request, "contact.html")

def members(request):
  return render(request, "members_list.html")

def members_detail(request):
  return render(request, "members_detail.html")