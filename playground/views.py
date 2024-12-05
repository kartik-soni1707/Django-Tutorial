from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, OrderItem

def say_hello(request):
    query_set=OrderItem.objects.filter(product__collection__id=1)
    return render(request,'hello.html', {'name': 'Jacob', 'result': list(query_set)})
