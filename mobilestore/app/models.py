from django.db import models

from account.models import CustUser

from datetime import datetime

# Create your models here.
PRODUCT_CHOICES=(
    ('AP','Apple'),
    ('SM','Samsung'),
    ('ON','Oneplus'),
    ('MI','Xiaomi'),
    ('vv','Vivo'),
    ('NO','Nokia'),

)
class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    discount_price=models.FloatField()
    category=models.CharField(choices=PRODUCT_CHOICES,max_length=5)
    product_image=models.ImageField(upload_to='product')
    def __self__(self):
        return self.title
    


class Cart(models.Model):
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE)
    Product= models.ForeignKey(Product, on_delete=models.CASCADE)
   
class Review(models.Model):
    comment=models.CharField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='commented_user')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='commented_product')

class Buy(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
   