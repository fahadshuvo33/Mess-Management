from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, default="N/A")  
    mess_name = models.CharField(max_length=100, default="Mess")  
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    custom_field = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
