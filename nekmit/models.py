from django.db import models

# Create your models here.

class representative:
    name :str
    gender :str
    age : int
    phonenumber : int
    state : bool
class business(models.Model):
    name =models.CharField(max_length=50)
    revenue =models.IntegerField(default=0)
    profit =models.IntegerField(default=0)
    shop_owner =models.CharField(max_length=50)
    phone_number =models.IntegerField(default=1)