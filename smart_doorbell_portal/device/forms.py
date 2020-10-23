from django import forms


class DeviceRegistrationForm():
    device_id = forms.CharField(max_length=50)
