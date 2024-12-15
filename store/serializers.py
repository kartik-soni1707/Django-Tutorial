from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=['id','title','products_count']
    products_count=serializers.SerializerMethodField(method_name='calucalte')
    def calucalte(self, collection:Collection):
        return collection.products.count()
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','unit_price','collection','price_with_tax', 'slug','inventory','description']
    price_with_tax=serializers.SerializerMethodField(method_name='calucalte')
    def calucalte(self, product:Product):
        return product.unit_price* Decimal(1.41)