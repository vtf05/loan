from django.db import models

from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from datetime import date

class User(AbstractUser):
    
 
    location=models.CharField(max_length=200,blank=True)
    latitude=models.CharField(max_length=50,blank=True)
    longitude=models.CharField(max_length=50,blank=True)
    
    
     
       
# Create your models here.
class owner(models.Model):
    
    name= models.CharField(max_length=50,default="bot")
    mobile_no= models.IntegerField()
    adhar= models.IntegerField(primary_key=True)
    Address=models.CharField(max_length=100)
    avatar1 = models.ImageField(blank=True)
    avatar2 = models.ImageField(blank=True)
    avatar3 = models.ImageField(blank=True)
    avatar4 = models.ImageField(blank=True)
    def __str__(self):
        return self.name

    def to_dict(self):
        return {'name':self.name,'mobile_no':self.mobile_no,
        'adhar':self.adhar,     'Address':self.Address,
        "avatar1":self.avatar1, "avatar2":self.avatar2,
        "avatar3":self.avatar3, "avatar4":self.avatar4  }
     