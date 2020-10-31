from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Device(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=50)
    device_nickname = models.CharField(null=True, blank=True, max_length=20)
    confirmation_code = models.CharField(max_length=5, default='NPSRE')

    def is_connected(self):
        if self.user == '':
            return False
        return True
