from django.db import models

# Create your models here.

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=500, unique=True)
    vehicle_name = models.CharField(max_length=500)
    vehicle_access_token = models.CharField(max_length=500)
    vehicle_refresh_token = models.CharField(max_length=500)
    vehicle_location_latitude = models.CharField(max_length=500)
    vehicle_location_longitude = models.CharField(max_length=500)
    vehicle_destination_latitude = models.CharField(max_length=500)
    vehicle_destination_longitude = models.CharField(max_length=500)


