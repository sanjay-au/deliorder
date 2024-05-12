from django.contrib.auth.decorators import login_required
from food.models import MealType,CuisineType,Custom_User

from cart.models import Cart,Order


def count(request):
    if (request.user.id==None):
        user=None
    else:
        user = request.user
    cart=Cart.objects.filter(user=user)
    total=0
    for i in cart:
        total+=i.quantity
    return {'count':total}