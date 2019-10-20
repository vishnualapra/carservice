from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializer
from rest_framework import status

# Create your views here.


class Manufacturer(APIView):

    def get(self,request):
        try:
            manufacturer = models.Manufacturer.objects.all()
            ser = serializer.ManufacturerSer(manufacturer,many=True)
            success = True
            data = ser.data
            error = None
            stat = status.HTTP_200_OK
        except:
            success = False
            data = None
            error = "Error Occured"
            stat = status.HTTP_400_BAD_REQUEST
        return Response({'success':success,'data':data,'errors':error},status=stat)

    def put(self,request,id):
        try:
            manufacturer = models.Manufacturer.objects.get(id=id)
            if len(request.data) == 0:
                success = False
                data = None
                error = "atleat one field required to update"
                stat = status.HTTP_400_BAD_REQUEST

        except:
            success = False
            data = None
            error = "Invalid Id"
            stat = status.HTTP_400_BAD_REQUEST

        return Response({'success': success, 'data': data, 'errors': error}, status=stat)
