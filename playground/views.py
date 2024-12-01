from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    ok=calculate()
    return render(request,'hello.html', {'name': 'Jacob'})

def calculate():
    x=1
    y=2
    return x