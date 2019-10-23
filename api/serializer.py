from rest_framework import serializers
from . import models
from django.core.exceptions import ValidationError


class ManufacturerSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Manufacturer


class ModelSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Model


class CarSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Car


class MechanicSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Mechanic


class MechanicSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Mechanic


class CustomerSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Customer


class BookingSer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Booking
