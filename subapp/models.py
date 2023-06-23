from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    S_no = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Notes = models.CharField(max_length=10000,null=True)
    created_at=models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    profile_name=models.CharField(max_length=100)
    screen_access=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.profile_name
    
class CreateUser(models.Model):
    st=(
        ('active','Active'),
        ('inactive','Inactive')
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    user_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    user_profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=st)