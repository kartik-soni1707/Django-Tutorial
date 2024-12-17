from rest_framework import serializers
from .models import Product, Collection, Review
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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields=['id','name','description','date']
    def create(self, validated_data):
        product_id=self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
        