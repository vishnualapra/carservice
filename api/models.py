from django.db import models

# Create your models here.

#manufacturer
class Manufacturer(models.Model):
    manufacturer_code = models.AutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=100)
    manufacturer_detail = models.TextField()

    def __str__(self):
        return self.manufacturer_name


class Model(models.Model):
    mode_code = models.AutoField(primary_key=True)
    daily_hire_rate = models.IntegerField()
    model_name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.PROTECT)

    def __str__(self):
        return self.model_name



class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    mechanic_name = models.CharField(max_length=100)
    other_mechanic_details = models.TextField()

    def __str__(self):
        return self.mechanic_name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=500)
    address_line_2 = models.CharField(max_length=500)
    address_line_3 = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    other_customer_details = models.TextField()

    def __str__(self):
        return self.last_name


class Car(models.Model):
    license_number = models.AutoField(primary_key=True)
    current_milage = models.CharField(max_length=50)
    engine_size = models.CharField(max_length=50)
    other_car_details = models.TextField()
    model = models.ForeignKey(Model,on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

    def __str__(self):
        return self.license_number


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    datetime_of_service = models.DateTimeField()
    payment_received_yn = models.BooleanField(default=False)
    other_bookin_details = models.TextField()
    car = models.ForeignKey(Car,on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    mechanic = models.ForeignKey(Mechanic,on_delete=models.PROTECT)
