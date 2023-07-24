from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1> hi hello</h>')
def second(request):
    return HttpResponse('<h1> hi word</h1>')