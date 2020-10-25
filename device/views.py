from django.shortcuts import render, redirect
from .forms import DeviceRegistrationForm

from django.contrib import messages

# Create your views here.


def device_registration(request):
    if request.method == 'POST':
        device_form = DeviceRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your device has successfully been linked!')
            return redirect('profile')
    else:
        device_form = DeviceRegistrationForm()
    return render(request, 'device/register.html', {'device_form': device_form})
