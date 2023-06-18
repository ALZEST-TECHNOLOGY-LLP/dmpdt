from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


# Create your models here.
class deviced(models.Model):
    device_id = models.CharField("", max_length=65,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    vehicle_number = models.CharField("", max_length=65,unique=True)
    vehicle_name = models.CharField("", max_length=65)
    lat = models.FloatField(blank=True,null=True)
    long = models.FloatField(blank=True,null=True)
    is_online = models.BooleanField(default=False)
    def __str__(self):
        return self.device_id
    
    


class SensorData(models.Model):
    device = models.ForeignKey(deviced, on_delete=models.CASCADE)
    vibration = models.FloatField(null=True)
    gaslink = models.FloatField(null=True)
    temperaturea = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    temperatured = models.FloatField(null=True)
    voltage = models.FloatField(null=True)
    fangle = models.FloatField(null=True)
    sensor_data_8 = models.FloatField(null=True)
    sensor_data_9 = models.FloatField(null=True)
    sensor_data_10 = models.FloatField(null=True)
    timed = models.DateTimeField(null=True)