from django.urls import path

from .views import device_registration


urlpatterns = [
    path('register/', device_registration, name='device_registration'),
    ]
