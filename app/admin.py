from django.contrib import admin
from .models import Location, WeatherForecast

# Register your models here.
admin.site.register(Location)
admin.site.register(WeatherForecast)