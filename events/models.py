from django.db import models
from datetime import datetime
import string
import random
# Create your models here.


class Event(models.Model):
    device_id = models.IntegerField(default=1)
    event_type = models.CharField(max_length=10)

   
