from django.contrib import admin
from food.models import MealType,CuisineType,FoodItems,Custom_User
# Register your models here.
admin.site.register(MealType)
admin.site.register(CuisineType)
admin.site.register(FoodItems)
admin.site.register(Custom_User)