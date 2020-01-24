from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey ProMazo Fam! You're at the quiz index.")
