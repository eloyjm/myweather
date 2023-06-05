from django.urls import path
from .views import Home, LocationList, WeatherList, WeatherByLocationList, WeatherCreate, LocationCreate

urlpatterns = [
    path('', Home, name='home'),
    path('locations/', LocationList.as_view(), name='location-list'),
    path('locations/create/', LocationCreate.as_view(), name='location-create'),
    path('weather/', WeatherList.as_view(), name='weather-list'),
    path('weather/create/', WeatherCreate.as_view(), name='weather-create'),
    path('weather/<int:id>/', WeatherByLocationList.as_view(), name='weather-by-location-list'),
]
