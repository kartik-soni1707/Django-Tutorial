from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import ProductSerializer, CollectionSerializer
from rest_framework import status
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer 
    lookup_field= 'id'
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['id']).count()>0:
            return Response({'error':'Product cant be deleted since it has an orderitem'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)    

class CollectionViewSet(ModelViewSet):
    queryset= Collection.objects.all()
    serializer_class= CollectionSerializer 
    lookup_field= 'id'
    def delete(self,request,id):
        collection=get_object_or_404(Collection, pk=id)
        if collection.products.count()>0:
            return Response({'error':'Collection cant be deleted since it has an product'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    