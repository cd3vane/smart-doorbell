# Generated by Django 3.1.2 on 2020-12-03 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0006_remove_device_user'),
        ('users', '0004_remove_profile_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.device'),
        ),
    ]