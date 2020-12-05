from django.urls import path

from .views import device_registration, device_control


urlpatterns = [
    path('register/', device_registration, name='device_registration'),
    path('control/', device_control, name='device_control'),

    ]
