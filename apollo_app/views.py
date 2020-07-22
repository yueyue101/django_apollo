from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print("暑促")
    return HttpResponse("index")

def login(request):
    return HttpResponse("login")