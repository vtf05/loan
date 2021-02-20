from rest_framework import serializers
from api.models import  owner

        
class ownerSerializer(serializers.ModelSerializer):

     
    class Meta:
        model = owner
        fields = ('name','DPS','Gyroscope','BPS','Address','vehicle','vehicle_no','vehicle_pol',"avatar")