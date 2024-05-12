from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from food.models import FoodItems,MealType,CuisineType,Custom_User


# Create your views here.
def home(request):
    s_messages=messages.get_messages(request)
    food=FoodItems.objects.filter(is_today_special=True)
    meal=MealType.objects.all()
    cuisine=CuisineType.objects.all()
    return render(request,'home.html',{'k':food,'meal':meal,'cuisine':cuisine,'messages':s_messages})

def menu(request):
    all=FoodItems.objects.all()
    return render(request,'items.html',{'menu':all})

def mealtype_menu(request,id):
    m=MealType.objects.get(id=id)
    if m.name=='All':
        return redirect('food:menu')
    else:
        detail=FoodItems.objects.filter(mealType=id)
        return render(request,'items.html',{'menu':detail})
def cuisine_menu(request,id):
    menu=FoodItems.objects.filter(cuisine=id)
    return render(request,'items.html',{'menu':menu})

def food_detail(request,id):
    f=FoodItems.objects.get(id=id)
    return render(request,'detail.html',{'f':f})

def register(request):
    if(request.method=='POST' and request.FILES.get('profile')):
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        phone=request.POST['phone']
        profile=request.FILES['profile']
        email=request.POST['email']
        try:
            if password==cpassword:
                user=Custom_User.objects.create_user(username=username,password=password,first_name=f_name,last_name=l_name,email=email,phone=phone,profile=profile)
                user.save()
                user=authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    messages.success(request,"User Registration Successful")
                    return redirect('food:home')
            else:
                messages.error(request, 'Passwords are not same')
        except IntegrityError:
            messages.error(request, 'Username Exist try using different')

    return render(request,'register.html')

def user_login(request):
    msg=None
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            try:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('food:home')
            except:
                messages.error(request,'Invalid Credentials')
        else:
            messages.error(request,"No User Found")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('food:login')

@login_required
def account(request):
    s_messages=messages.get_messages(request)
    user=request.user
    return render(request,'account.html',{'user':user,'messages':s_messages})

@login_required
def change_password(request):
    if(request.method=='POST'):
        user=request.user
        username=user.username
        new_password=request.POST['new_password']
        cp=request.POST['cpassword']
        if new_password==cp:
            user.password=make_password(new_password)
            user.save()
            user = authenticate(username=username, password=new_password)
            if user:
                login(request, user)
                messages.success(request, "Password Changed Successfully")
                return redirect('food:account')
        else:
            messages.error(request,"Passwords must be Same")
    return render(request,'changepassword.html')

@login_required
def user_delete(request):
    user=request.user
    user.delete()
    messages.success(request, "Account Deleted Successfully")
    return redirect('food:home')