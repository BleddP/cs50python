from django.shortcuts import render

tasks = ['Foo', 'Bar', 'Baz']

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html')