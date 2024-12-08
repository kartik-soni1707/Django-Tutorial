from django.db import models

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=120)
    featured_product=models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering= ['title']
class Product(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField()
    description=models.TextField()
    unit_price=models.DecimalField(decimal_places=2,max_digits=10)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField('Promotion', blank=True,)
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering= ['title']

class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='B'
    MEMBERSHIP_GOLD='B'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ] 
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=120)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    class Meta:
        ordering= ['first_name', 'last_name']
    


class Order(models.Model):
    payment_status=[('P','Pending'),('C','Completed'),('F','Failed')] 
    
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1, choices=payment_status, default='P')
    customer=models.ForeignKey(Customer, on_delete=models.PROTECT)

class Address(models.Model):
    street=models.CharField(max_length=120)
    city=models.CharField(max_length=120)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip=models.CharField(max_length=120)

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.PROTECT)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(decimal_places=2,max_digits=6)

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()

class Promotion(models.Model):
    description=models.CharField(max_length=120)
    discount=models.DecimalField(decimal_places=2,max_digits=3)


