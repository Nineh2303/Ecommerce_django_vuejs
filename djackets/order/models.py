from django.contrib.auth.models  import User
from django.db import models
                    
from product.models import  Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE ,default ='')
    first_name= models.CharField(max_length=100 ,null = True)
    last_name= models.CharField(max_length=100 ,null= True)
    email= models.CharField(max_length=100 , null = True)
    address= models.CharField(max_length=100 , null =True)
    zipcode= models.CharField(max_length=100,null = True)
    place= models.CharField(max_length=100,null = True)
    phone= models.CharField(max_length=100,null = True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    paid_amount = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    stripe_token = models.CharField(max_length=100 ,blank = True)
    
    class Meta: 
        ordering =['-created_at',]

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price =models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
