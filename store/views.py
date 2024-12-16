from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
from rest_framework import status
# Create your views here.

class ProductList(APIView):
    def get(self,request):
        queryset=Product.objects.select_related('collection').all()
        serializer=ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)        


class ProductDetails(APIView):
    def get(self,request):
        product=get_object_or_404(Product, pk=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request):
        product=get_object_or_404(Product, pk=id)
        serializer=ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request):
        product=get_object_or_404(Product, pk=id)
        if product.orderitems.count()>0:
            return Response({'error':'Product cant be deleted since it has an orderitem'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionList(APIView):
    def get(self,request):
        queryset=Collection.objects.all()
        serializer=CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    def put(self,request):
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CollectionDetails(APIView):
    def get(self,request):
        collection=get_object_or_404(Collection, pk=id)
        serializer=CollectionSerializer(collection)
        return Response(serializer.data)
    def put(self,request):
        collection=get_object_or_404(Collection, pk=id)
        serializer=CollectionSerializer(collection,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request):
        collection=get_object_or_404(Collection, pk=id)
        if collection.products.count()>0:
            return Response({'error':'Collection cant be deleted since it has an product'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)