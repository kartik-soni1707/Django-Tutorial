from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
from rest_framework import status
# Create your views here.

class ProductList(ListCreateAPIView):
    queryset= Product.objects.select_related('collection').all()
    serializer_class= ProductSerializer 
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset= Product.objects.select_related('collection').all()
    serializer_class= ProductSerializer
    lookup_field= 'id'
    

class CollectionList(ListCreateAPIView):
    queryset= Collection.objects.all()
    serializer_class= CollectionSerializer 

class CollectionDetails(RetrieveUpdateDestroyAPIView):
    queryset= Collection.objects.all()
    serializer_class= CollectionSerializer
    lookup_field= 'id'
    