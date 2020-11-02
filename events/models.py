from django.db import models
from datetime import datetime
import string
import random

# Create your models here.


class Event(models.Model):
    DOORBELL = 'Doorbell'
    LOCKED = 'Lock'
    UNLOCKED = 'Unlock'
    EVENT_TYPE_CHOICES = [
        (DOORBELL, 'Doorbell'),
        (LOCKED, 'Locked'),
        (UNLOCKED, 'Unlocked')
    ]
    event_id = random.choice(string.digits)
    timestamp = models.DateTimeField()
    event_type = models.CharField(
        max_length=10,
        choices=EVENT_TYPE_CHOICES,
        default=DOORBELL
    )

    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        super().save(*args, **kwargs)
