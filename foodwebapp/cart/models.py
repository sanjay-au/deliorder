from django.db import models
from food.models import FoodItems,Custom_User

# Create your models here.

class Cart(models.Model):
    food_item=models.ForeignKey(FoodItems,on_delete=models.CASCADE)
    user=models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    quantity=models.DecimalField(max_digits=3,decimal_places=0,default=1)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.food_item.name
    def subtotal(self):
        return self.quantity * self.food_item.price

class Order(models.Model):
    food_item=models.ForeignKey(FoodItems,on_delete=models.CASCADE)
    user=models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    quantity=models.DecimalField(max_digits=3,decimal_places=0,default=1)
    address=models.TextField(default='')
    phone=models.DecimalField(max_digits=10,decimal_places=0,default=0)
    order_date=models.DateTimeField(auto_now_add=True)
    choices=(('Pending','Pending'),('Order Picked','Order Picked'),('Out For Delivery','Out For Delivery'),('Delivered','Delivered'))
    pay=(('Paid','Paid'),('Cash On Delivery','Cash On Delivery'))
    order_status=models.CharField(max_length=20,choices=choices)
    amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_status=models.CharField(max_length=20,choices=pay,default='')
    def __str__(self):
        return self.food_item.name
    def subtotal(self):
        return self.quantity * self.amount


