from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Device(models.Model):
    user = User.username
    device_id = models.CharField(max_length=50)
    device_nickname = models.CharField(max_length=20)

    def is_connected(self):
        if self.user == '':
            return False
        return True
