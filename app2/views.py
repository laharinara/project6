from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1> hi hello</h1>')
def second(request):
    return HttpResponse('<h1> hi world</h1>')
