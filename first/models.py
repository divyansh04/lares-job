from operator import mod
from re import M

from django.db import models

class User(models.Model):

    fullname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    username=models.CharField(max_length=30)
    #address=models.CharField(max_length=30)
    pincode=models.IntegerField()
    password=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    dob=models.DateField()
    martialstatus=models.CharField(max_length=20)
    genter=models.CharField(max_length=20)
    adhaarnum=models.IntegerField()
    introdution=models.CharField(max_length=40,blank="no intro")


# Create your models here.
