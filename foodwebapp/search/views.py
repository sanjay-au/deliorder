from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from food.models import FoodItems

# Create your views here.

def search(request):
    s=None
    food_items=''
    if request.method=='POST':
        s=request.POST.get('search')
        if s!=' ' and s!= '':
            food_items=FoodItems.objects.filter(Q(name__icontains=s) | Q(mealType__name__icontains=s) | Q(cuisine__name__icontains=s))
        elif s=='' or s==' ':
            return redirect('food:home')
        else:
            food_items=None
    return render(request,'search.html',{'search':s,'menu':food_items})
