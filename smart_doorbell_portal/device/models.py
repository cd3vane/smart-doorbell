from django.db import models

# Create your models here.


class Device(models.Model):
    device_id = models.CharField(max_length=50)
    
