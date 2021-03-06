from django.shortcuts import render, redirect
from .forms import DeviceRegistrationForm

from django.contrib import messages
from .models import Device
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def device_control(request):
    return render(request, 'device/device_control2.html')
