from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cart.models import Cart,Order
from food.models import FoodItems


# Create your views here.
@login_required
def AddCart(request,id):
    if (request.method == 'POST'):
        if 'order' in request.POST:
            qty = request.POST.get('qty')
            request.session['qty']=qty
            request.session['my_id']=id
            return redirect('cart:orderform_id')
        elif 'cart' in request.POST:
            qty = request.POST.get('qty')
            food_item=FoodItems.objects.get(id=id)
            u=request.user
            try:
                cart = Cart.objects.get(user=u,food_item=food_item)
                if (food_item.stock > 0 and int(qty) < int(food_item.stock)):
                    cart.quantity += int(qty)
                    cart.save()
                    food_item.stock -= int(qty)
                    food_item.save()
                    messages.success(request,'Added to Your Cart')
                else:
                    messages.error(request,'Unavailability of Stocks Please Check your Quantity')
            except Cart.DoesNotExist:
                if (food_item.stock > 0 and int(qty) < int(food_item.stock)):
                    cart = Cart.objects.create(food_item=food_item, user=u, quantity=int(qty))
                    cart.save()
                    food_item.stock -= int(qty)
                    food_item.save()
                    messages.success(request, 'Added to Your Cart')
                else:
                    messages.error(request,'Unavailability of Stocks Please Check your Quantity')
            return redirect('cart:cart')

@login_required
def cartview(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    total=0
    for i in cart:
        total=total + (i.quantity * i.food_item.price)
    return render(request,'cartview.html',{'cart':cart,'total':total})
@login_required
def add_cart(request,id):
    food_item=FoodItems.objects.get(id=id)
    user=request.user
    try:
        cart = Cart.objects.get(user=user, food_item=food_item)
        if (food_item.stock > 0 ):
            cart.quantity += 1
            cart.save()
            food_item.stock -= 1
            food_item.save()
    except Cart.DoesNotExist:
        if (food_item.stock > 0):
            cart = Cart.objects.create(food_item=food_item, user=user, quantity=1)
            cart.save()
            food_item.stock -= 1
            food_item.save()
    return redirect('cart:cart')
@login_required
def remove_cart(request,id):
    food_items=FoodItems.objects.get(id=id)
    user=request.user
    try:
        cart=Cart.objects.get(food_item=food_items,user=user)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()
            food_items.stock+=1
            food_items.save()
        else:
            cart.delete()
            food_items.stock+=1
            food_items.save()
            messages.success(request,'Item Removed from Cart')
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cart')
@login_required
def delete_cart(request,id):
    food_item=FoodItems.objects.get(id=id)
    user=request.user
    try:
        cart=Cart.objects.get(food_item=food_item,user=user)
        food_item.stock+=cart.quantity
        food_item.save()
        cart.delete()
        messages.success(request, 'Item Removed from Cart')
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cart')
@login_required
def orderview(request):
    user=request.user
    order=Order.objects.filter(user=user)
    return render(request,'orderview.html',{'order':order})
@login_required
def orderform(request):
    if (request.method=='POST'):
        user=request.user
        cart=Cart.objects.filter(user=user)
        add=request.POST['address']
        payment=request.POST['payment']
        total=0
        for i in cart:
            total+=i.quantity * i.food_item.price
        if payment=='Paid':
            pass
        else:
            try:
                for i in cart:
                    o=Order.objects.create(food_item=i.food_item,user=user,quantity=i.quantity,address=add,payment_status=payment,order_status='Pending',amount=total)
                    o.save()
                    cart.delete()
                messages.success(request,"Your Order has been Placed")
                return redirect('cart:orderview')
            except:
                messages.error(request,"Unable to Place Your Order")
    return render(request,'orderform.html')

def order_form(request):
    id=request.session.get('my_id')
    qty=request.session.get('qty')
    if (request.method=='POST'):
        user=request.user
        food=FoodItems.objects.get(id=id)
        add=request.POST['address']
        payment=request.POST['payment']
        amount=int(qty) * food.price
        try:
            o=Order.objects.create(food_item=food,user=user,quantity=qty,address=add,payment_status=payment,order_status='Pending',amount=amount)
            o.save()
            messages.success(request, "Your Order has been Placed")
            return redirect('cart:orderview')
        except:
            messages.error(request,"Unable to Place Your Order")
    return render(request,'orderform.html')

@login_required
def admin_order_list(request):
    order=Order.objects.exclude(order_status='Delivered').order_by('order_date')
    return render(request,'adminorder.html',{'order':order})

@login_required
def admin_view(request,id):
    order = Order.objects.get(id=id)
    if request.method=="POST":
        o=request.POST['order']
        order.order_status=o
        order.save()
        messages.success(request,'Order Status Updated Successfully')
        return redirect('cart:adminlist')
    return render(request,'adminview.html',{'f':order})