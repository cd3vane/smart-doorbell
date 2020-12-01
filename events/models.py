from django.db import models
from django.utils import timezone
import string
import random
# Create your models here.


class Event(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    device_id = models.CharField(max_length=10)
    event_type = models.CharField(max_length=10)

   
    def __str__(self):
        return self.device_id