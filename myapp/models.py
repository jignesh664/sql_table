from django.db import models

# Create your models here.

class Customer(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    mobile=models.CharField(max_length=13)
    address=models.TextField()
    date=models.DateField()
    state=models.CharField(max_length=100,default='SOME STRING')
    city=models.CharField(max_length=100,default='SOME STRING')
    is_active=models.BooleanField(default=False)


    def __str__(self):
        return self.fname+" "+self.lname

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_model=models.CharField(max_length=100)
    product_price=models.CharField(max_length=100)
    product_model_year=models.CharField(max_length=100)
    product_color=models.CharField(max_length=100)
    date=models.DateField()   

    def __str__(self):
        return self.product_name+" "+self.product_model

class Order(models.Model):
    customer_id=models.ForeignKey(Customer,on_delete=models.PROTECT,null=True,blank=True)
    product_id=models.ForeignKey(Product,on_delete=models.PROTECT,null=True,blank=True)
    order_date=models.DateField() 
    order_number=models.CharField(max_length=100)
    order_price=models.CharField(max_length=100)

    def __str__(self):
        return self.order_price+" "+self.order_number
