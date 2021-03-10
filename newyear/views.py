from django.shortcuts import render
import datetime

items = ['Foo', 'Bar', 'Baz']

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'newyear/index.html', {
        "newyear": now.month == 1 and now.day == 1
    })

def tasks(request):
    return render(request, 'newyear/tasks.html', {
        'items': items
    })

def add(request):
    return render(request, 'newyear/addtask.html')