from django.shortcuts import render, redirect
from .forms import DeviceRegistrationForm

from django.contrib import messages
from .models import Device
# Create your views here.


def device_registration(request):
    if request.method == 'POST':
        device_form = DeviceRegistrationForm(request.POST)
        if device_form.is_valid():
            device_form.save()
            messages.success(request, f'Your device has successfully been linked!')
            return redirect('profile')
    else:
        device_form = DeviceRegistrationForm()
    return render(request, 'device/register_device.html', {'device_form': device_form})


def device_control(request):
    return render(request, 'device/device_control.html')
