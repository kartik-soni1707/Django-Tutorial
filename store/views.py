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
    def delete(self,request,id):
        product=get_object_or_404(Product, pk=id)
        if product.orderitems.count()>0:
            return Response({'error':'Product cant be deleted since it has an orderitem'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CollectionList(ListCreateAPIView):
    queryset= Collection.objects.all()
    serializer_class= CollectionSerializer 

class CollectionDetails(RetrieveUpdateDestroyAPIView):
    queryset= Collection.objects.all()
    serializer_class= CollectionSerializer
    lookup_field= 'id'
    def delete(self,request,id):
        collection=get_object_or_404(Collection, pk=id)
        if collection.products.count()>0:
            return Response({'error':'Collection cant be deleted since it has an product'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    