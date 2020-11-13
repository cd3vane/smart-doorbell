from django.db import models
from datetime import datetime
import string
import random

# Create your models here.


class Event(models.Model):
    device_id = models.IntegerField(max_length=50)
    event_id = models.IntegerField(max_length=20)
    event_type = models.CharField(max_length=10)

   
