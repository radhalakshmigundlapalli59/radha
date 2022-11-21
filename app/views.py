from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def propose(request):
    return HttpResponse('<marquee>i love u too</marquee>')

def reject(request):
    return HttpResponse('<marquee>sorry bro</marquee>')