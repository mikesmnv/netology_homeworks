from django.urls import path

from app import views


urlpatterns = [
    path('landing/index/', views.index, name='index'),
    path('landing_alternate/index/', views.index, name='index'),
    path('landing/', views.landing, name='landing'),
    path('stats/', views.stats, name='stats'),
]
