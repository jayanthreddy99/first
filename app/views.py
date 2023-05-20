from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def srujana(request):
    return HttpResponse('<marquee><h1>srujana tinava raa.. vadhilesthunava raa</h1></marquee>')

def revi(request):
    return HttpResponse("<i><h1>it's Not ravi It's Revi...🤣🤣")