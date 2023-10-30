from django.contrib.auth.models import AbstractUser
from django.db import models

class Mess_Admin(models.Model):
    name = models.CharField(max_length=30, unique=True,default='N/A')

    def __str__(self):
        return self.name

class Mess(models.Model):
    name = models.CharField(max_length=100,default='N/A')
    admin = models.ForeignKey(Mess_Admin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, default="N/A")  
    is_admin = models.BooleanField(default=True)
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE ,null=True, blank=True )

    def __str__(self):
        return self.username
