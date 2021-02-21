from rest_framework import serializers
from api.models import  owner

        
class ownerSerializer(serializers.ModelSerializer):

     
    class Meta:
        model = owner
        fields = ('name','mobile_no',"adhar",'Address',"avatar1","avatar2","avatar3","avatar4")