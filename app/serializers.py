from rest_framework import serializers
from app.models import Location, WeatherForecast

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'country']

class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = ['id','location', 'date', 'time', 'temperature', 'humidity', 'description']