from rest_framework import generics
from app.models import Location, WeatherForecast
from .serializers import LocationSerializer, WeatherForecastSerializer
from django.shortcuts import render

# Create your views here.
class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class WeatherList(generics.ListAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

class WeatherByLocationList(generics.ListAPIView):
    serializer_class = WeatherForecastSerializer

    def get_queryset(self):
            location = self.kwargs['id']
            return WeatherForecast.objects.filter(location__id=location)

class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class WeatherCreate(generics.CreateAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer

def Home(request):
    routes = [
        'locations/',
        'locations/create/',
        'weather/',
        'weather/create/',
    ]

    return render(request, 'home.html', {'routes': routes})