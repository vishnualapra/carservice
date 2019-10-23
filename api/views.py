from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
import datetime
# Create your views here.



class ManuFacturer(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,AllowAny)
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializer.ManufacturerSer


class Model(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,AllowAny)
    queryset = models.Model.objects.all()
    serializer_class = serializer.ModelSer


class Car(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,AllowAny)
    queryset = models.Car.objects.all()
    serializer_class = serializer.CarSer


class Mechanic(viewsets.ModelViewSet):

    queryset = models.Mechanic.objects.all()
    serializer_class = serializer.MechanicSer


class Customer(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,AllowAny)
    queryset = models.Customer.objects.all().order_by('-created_at')
    serializer_class = serializer.CustomerSer


class BookingToday(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,AllowAny)
    queryset = models.Booking.objects.filter(service_date=datetime.datetime.today().date()).order_by('-service_date')
    serializer_class = serializer.BookingSer


class Booking(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,AllowAny)
    queryset = models.Booking.objects.all().order_by('-service_date')
    serializer_class = serializer.BookingSer


class filter_model(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, AllowAny)
    def get(self,request,id):
        data =models.Model.objects.filter(manufacturer__manufacturer_code=id)
        ser = serializer.ModelSer(data,many=True)
        return Response(ser.data)



class filter_car(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, AllowAny)
    def get(self,request,id):
        data =models.Car.objects.filter(customer__customer_id=id)
        ser = serializer.CarSer(data,many=True)
        return Response(ser.data)

class available(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, AllowAny)

    def get(self,request,id):
        data =models.Model.objects.get(model_code=id)
        daily_limit = data.daily_hire_rate
        bookings = models.Booking.objects.filter(service_date__gte=datetime.datetime.today(),car__model__model_code=id)
        book_count = bookings.count()
        diff =int(book_count / daily_limit)
        daily_queue = int(book_count%daily_limit)+1
        date = datetime.datetime.today().date() + datetime.timedelta(days=diff)
        return Response({'daily_limit':daily_limit,'count':book_count,'available_date':date,'daily_queue':daily_queue})


class caron(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self,request,id):
        try:
            data =models.Car.objects.get(license_number=id)
            if data.on_service == True:
                data.on_service = False
            else:
                data.on_service = True
            data.save()
            stat = status.HTTP_200_OK
            data = {'on_service':data.on_service}
            suc = True
        except:
            stat = status.HTTP_400_BAD_REQUEST
            suc = False
            data = None
        return Response({'success':suc,'data':data},status=stat)


class paid(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self,request,id):
        try:
            data = models.Booking.objects.get(booking_id=id)

            data.payment_received_yn = True
            data.save()
            stat = status.HTTP_200_OK
            suc = True
        except:
            stat = status.HTTP_400_BAD_REQUEST
            suc = False

        return Response({'success':suc},status=stat)


class delivered(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, AllowAny)
    def post(self,request,id):
        try:
            data = models.Booking.objects.get(booking_id=id)
            data.completed = True
            data.payment_received_yn = True
            data.car.on_service = False
            data.car.save()
            data.save()
            stat = status.HTTP_200_OK
            suc = True
        except:
            stat = status.HTTP_400_BAD_REQUEST
            suc = False

        return Response({'success':suc},status=stat)
