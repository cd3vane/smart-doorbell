from django.urls import path

from .views import device_registration


urlpatterns = [
    path('add_device', device_registration, name='device_registration'),
    ]
