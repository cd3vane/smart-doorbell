from django.contrib import admin

# Register your models here.
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Device, DeviceAdmin)
