from django.db import models

# Create your models here.
class Location(models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WeatherForecast(models.Model):
    id = models.BigIntegerField(primary_key = True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.location} - {self.date} {self.time}"