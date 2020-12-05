from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mqtt.publisher.models import Data as MQTTData
# Create your models here.


class Device(models.Model):
    device_nickname = models.CharField(null=True, blank=True, max_length=20)
    confirmation_code = models.CharField(max_length=5, default='NPSRE')
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='owner_of')

  
@receiver(post_save, sender=MQTTData)
def auto_update(sender, instance, **kwargs):
     instance.update_remote()