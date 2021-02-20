from rest_framework import serializers
from api.models import  owner

        
class ownerSerializer(serializers.ModelSerializer):

     
    class Meta:
        model = owner
        fields = ('name','DPS','Gyroscope','BPS','Address','vehicle','vehicle_fuel','vehicle_pol',"avatar")