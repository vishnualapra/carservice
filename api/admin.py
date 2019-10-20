from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Manufacturer)
admin.site.register(models.Model)
admin.site.register(models.Car)
admin.site.register(models.Mechanic)
admin.site.register(models.Customer)
