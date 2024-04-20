from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ChargingStation(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=255)
    available_chargers = models.PositiveIntegerField(default=0)
    # Add other fields as per your requirements

    def __str__(self):
        return self.name

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    payment_datetime = models.DateTimeField(auto_now_add=True)
    slot_datetime = models.DateTimeField()
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as per your requirements

    def __str__(self):
        return f"{self.user.username} - {self.charging_station.name} - {self.payment_datetime}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    slot_time = models.DateTimeField()
    # Add other fields as per your requirements

    def __str__(self):
        return f"{self.user.username} - {self.charging_station.name} - {self.slot_time}"
