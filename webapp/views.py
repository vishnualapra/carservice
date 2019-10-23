from django.shortcuts import render,loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from api import models
import datetime
# Create your views here.

def login(request):
    print(request.user.id,'lll')
    if request.user.id != None:
        return HttpResponseRedirect('/dashboard/')
    temp = loader.get_template('webapp/login.html')
    return HttpResponse(temp.render({},request))

@login_required(login_url='/login/')
def dashboard(request):
    page = 'dashboard'
    no_cust = models.Customer.objects.all().count()
    no_order = models.Booking.objects.all().count()
    no_car = models.Car.objects.all().count()
    no_models = models.Model.objects.all().count()
    completed_orders = models.Booking.objects.filter(completed=True).count()
    pending_orders = models.Booking.objects.filter(completed=False).count()
    today_orders = models.Booking.objects.filter(service_date=datetime.datetime.today().date()).count()
    employees = models.Mechanic.objects.all().count()
    temp = loader.get_template('webapp/dashboard.html')
    return HttpResponse(temp.render({'page':page,'no_cust':no_cust,'no_car':no_car,'no_order':no_order,
                                     'no_models':no_models,'completed_orders':completed_orders,
                                     'pending_orders':pending_orders,'today_orders':today_orders,
                                     'employees':employees},request))


def index(request):
    return HttpResponseRedirect('/dashboard/')


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def mechanics(request):
    page = 'mechanic'
    temp = loader.get_template('webapp/mechanics.html')
    return HttpResponse(temp.render({'page': page}, request))


@login_required(login_url='/login/')
def manufacturer(request):
    page = 'manufacturer'
    temp = loader.get_template('webapp/manufacturer.html')
    return HttpResponse(temp.render({'page': page}, request))

@login_required(login_url='/login/')
def carmodels(request,id):
    page = 'models'
    temp = loader.get_template('webapp/models.html')
    data = models.Manufacturer.objects.get(manufacturer_code=id)
    mod = models.Model.objects.filter(manufacturer__manufacturer_code=id)
    return HttpResponse(temp.render({'page': page,'manu_id':id,'data':data,'mod':mod}, request))


@login_required(login_url='/login/')
def cars(request,id,idd):
    page = 'cars'
    temp = loader.get_template('webapp/neworder.html')
    data = models.Model.objects.get(model_code=idd)
    data2 = models.Manufacturer.objects.get(manufacturer_code=id)
    mod = models.Model.objects.filter(manufacturer__manufacturer_code=id)
    return HttpResponse(temp.render({'page': page,'manu_id':id,'data':data,'data2':data2,'mod':mod}, request))


@login_required(login_url='/login/')
def customers(request):
    page = 'booking'
    spage = 'customers'
    temp = loader.get_template('webapp/customers.html')
    return HttpResponse(temp.render({'page': page,'spage':spage}, request))


@login_required(login_url='/login/')
def bookcustomer(request,id):
    page = 'booking'
    spage = 'book'
    temp = loader.get_template('webapp/custorder.html')
    profile = models.Customer.objects.get(pk=id)
    return HttpResponse(temp.render({'page': page,'spage':spage,'profile':profile}, request))


@login_required(login_url='/login/')
def bookings(request):
    page = 'booking'
    spage = 'book'
    temp = loader.get_template('webapp/bookings.html')
    return HttpResponse(temp.render({'page': page,'spage':spage}, request))


@login_required(login_url='/login/')
def today(request):
    page = 'booking'
    spage = 'today'
    temp = loader.get_template('webapp/bookings.html')
    return HttpResponse(temp.render({'page': page,'spage':spage}, request))
