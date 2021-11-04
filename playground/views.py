from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    x = 1
    y = 2
    context = {'name': 'Fady'}
    return render(request, 'playground/hello.html', context)

