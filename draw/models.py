from django.db import models

# Create your models here.
class Drawer(models.Model):
    name=models.TextField(max_length=50,null=True)
    email=models.TextField(max_length=50,null=True)
    password=models.TextField(max_length=50,null=True)
    def __str__(self):
        return self.name
    class meta:
        dt_table="draw"

class Drawings(models.Model):
    drawing=models.ImageField(upload_to='pictures',null=True)
    name=models.TextField(max_length=50,null=True)
    price=models.FloatField(null=True)
    discription=models.TextField(max_length=500,null=True)
    def __str__(self):
        return self.name
    
class Seller(models.Model):
    username=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)
    def __str__(self):
        return self.username
class Cart(models.Model):
    customer=models.ForeignKey(Drawer,on_delete=models.CASCADE,null=True)
    drawings=models.ForeignKey(Drawings,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)

