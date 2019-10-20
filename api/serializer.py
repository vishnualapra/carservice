from rest_framework import serializers
from . import models


class ManufacturerSer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'
