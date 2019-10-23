"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('manufacturer', views.ManuFacturer, base_name='manufacturer')
router.register('model', views.Model, base_name='model')
router.register('car', views.Car, base_name='car')
router.register('mechanic', views.Mechanic, base_name='mechanic')
router.register('customer', views.Customer, base_name='customer')
router.register('booking', views.Booking, base_name='booking')
router.register('booking_today', views.BookingToday, base_name='bookingtoday')
urlpatterns = router.urls
urlpatterns = urlpatterns + [
    path('filter_model/<int:id>/',views.filter_model.as_view()),
    path('filter_car/<int:id>/', views.filter_car.as_view()),
    path('available_date/<int:id>/', views.available.as_view()),
    path('car_onservice/<int:id>/', views.caron.as_view()),
    path('paid/<int:id>/', views.paid.as_view()),
    path('delivered/<int:id>/', views.delivered.as_view()),

]
