from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import  ownerSerializer
from rest_framework.decorators import action
from . models import owner



class ownerViewSet(viewsets.ModelViewSet):
    queryset = owner.objects.all()
    serializer_class = ownerSerializer
    permission_classes = [IsAuthenticated]

    def create(self,request,*args,**kwargs):
        viewsets.ModelViewSet.create(self,request,*args,**kwargs)
        ob = owner.objects.latest("id")
        return Response({"status":"success","condition":y,"tmp":args})
       # return Response({"condition":y})

       
   
    def top(self,request):
        ob=owner.object.all()[:10]
        print(ob)
        print("function is called")
        return Response(ob)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)