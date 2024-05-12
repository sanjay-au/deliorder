from django.contrib.auth.decorators import login_required
from food.models import MealType,CuisineType,Custom_User


def meal(request):
    m = MealType.objects.all()
    c = CuisineType.objects.all()
    if request.user.id==None :
        user=None
    else:
        user=request.user
    return {'m':m,'c':c,'user':user}