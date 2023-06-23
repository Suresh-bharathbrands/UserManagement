from django.contrib.auth.models import User
from .models import *


def users_and_projects(request):
    if request.user.is_authenticated:
        #  user access
        access=CreateUser.objects.filter(user=request.user).first()
        print(access)
       
    else:
        access=''
    return {'access': access}