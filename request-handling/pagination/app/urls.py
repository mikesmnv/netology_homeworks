from django.urls import path

from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('bus_stations', views.bus_stations, name='bus_stations'),
]
