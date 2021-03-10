from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'babystore/index.html')

def bleddyn(request):
    return HttpResponse('Hello Bleddyn!')

def david(request):
    return HttpResponse('Hello David!')

def greet(request, name):
    return render(request, 'babystore/greet.html', {
        'name': name.capitalize()
    })