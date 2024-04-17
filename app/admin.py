from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ChargingStation, Booking, Token

admin.site.register(ChargingStation)
admin.site.register(Booking)
admin.site.register(Token)