from django.db import models

# Create your models here.
class owner(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50,default="bot")
    mobile_no= models.IntegerField()
    adhar= models.IntegerField()
    Address=models.CharField(max_length=100)
    avatar1 = models.ImageField(blank=True)
    avatar2 = models.ImageField(blank=True)
    avatar3 = models.ImageField(blank=True)
    avatar4 = models.ImageField(blank=True)
    def __str__(self):
        return self.name

    def to_dict(self):
        return {"id":self.id ,'name':self.name,'mobile_no':self.mobile_no,
        'adhar':self.adhar,     'Address':self.Address,
        "avatar1":self.avatar1, "avatar2":self.avatar2,
        "avatar3":self.avatar3, "avatar4":self.avatar4  }
     