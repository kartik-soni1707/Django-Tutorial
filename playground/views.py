from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F, Func, ExpressionWrapper, FloatField
from django.db.models.aggregates import Count, Sum, Min, Avg, Max
from store.models import Product, Customer, Collection, OrderItem, Order, Address, Cart
from datetime import datetime
def say_hello(request):
    cart= Cart()
    cart.save()
    cart1=Cart.objects.filter(created_at=cart.created_at)
    cart1.update(created_at=datetime.now())
    cart1.delete()
    
    return render(request,'hello.html', {'name': 'Jacob'})
    