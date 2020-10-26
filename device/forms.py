from django import forms
from .models import Device


class DeviceRegistrationForm(forms.ModelForm):
    device_id = forms.CharField(max_length=50)
    device_nickname = forms.CharField(max_length=50)

    class Meta:
        model = Device
        fields = [
            'device_id', 'device_nickname'
            ]
