from django.db import models
from django.conf import settings
from accounts.models import Mess,CustomUser

class Bazar_List(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    note = models.CharField(max_length=1000, null=True)
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s on {self.date}"

class Meal(models.Model) :
    date = models.DateField()
    meal = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}---{self.date}---{self.meal}"
