from django.db import models
import uuid

# Create your models here.

class Customer(models.Model):
    id              = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name            = models.CharField(max_length = 200)
    email           = models.CharField(max_length = 200, null = True)
    date_created    = models.DateTimeField(auto_now_add = True)
    date_updated    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name            = models.CharField(max_length = 200)
    def __str__(self):
        return self.name        

class Product(models.Model):
    CATEGORIES_CHOICES = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
    )
    id              = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name            = models.CharField(max_length = 200)
    price           = models.FloatField()
    description     = models.CharField(max_length = 200, null = True, blank=True)
    category        = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    tags            = models.ManyToManyField(Tag)
    date_created    = models.DateTimeField(auto_now_add = True)
    date_updated    = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    id              = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    customer        = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    product         = models.ForeignKey(Product,  null = True, on_delete=models.SET_NULL)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=20)
    date_created    = models.DateTimeField(auto_now_add = True)
    date_updated    = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.customer.name} - {self.product.name}'

