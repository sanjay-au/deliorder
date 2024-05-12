from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MealType(models.Model):
    name=models.CharField(max_length=20,default="All")
    image=models.ImageField(upload_to='meal',null=True,blank=True)
    def __str__(self):
        return self.name

class CuisineType(models.Model):
    name=models.CharField(max_length=20,default="")
    image=models.ImageField(upload_to='cuisine',null=True,blank=True)
    def __str__(self):
        return self.name

class FoodItems(models.Model):
    name=models.CharField(max_length=20,default='')
    desc=models.TextField(default='')
    mealType=models.ForeignKey(MealType,on_delete=models.CASCADE)
    cuisine=models.ForeignKey(CuisineType,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='foodItems',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.DecimalField(max_digits=3,decimal_places=0,default=0)
    date_added=models.DateTimeField(auto_now_add=True)
    is_today_special=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Custom_User(AbstractUser):
    phone=models.DecimalField(max_digits=10,decimal_places=0,default=0)
    profile=models.ImageField(upload_to="user",null=True,blank=True)