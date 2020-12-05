from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Device(models.Model):
    device_nickname = models.CharField(null=True, blank=True, max_length=20)
    confirmation_code = models.CharField(max_length=5, default='NPSRE')
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='owner_of')
