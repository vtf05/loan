from django.db import models

# Create your models here.
class owner(models.Model):
    name= models.CharField(max_length=50,default="bot")
    DPS = models.IntegerField()
    BPS = models.IntegerField()
    Gyroscope=models.IntegerField()
    Address=models.CharField(max_length=50)
    vehicle=models.CharField(max_length=50)
    vehicle_no = models.CharField(max_length=100,default="0")
    vehicle_pol = models.CharField(max_length=3,default="0")
    avatar = models.ImageField(blank=True)
    def __str__(self):
        return self.name

    def to_dict(self):
        return {'name':self.name,'DPS':self.DPS,
        'BPS':self.BPS, 'Gyroscope':self.Gyroscope,'Address':self.Address,
        'vehicle':self.vehicle,'vehicle_fuel':self.vehicle_no,'vehicle_pol':self.vehicle_pol,"avatar":self.avatar}
     