# Generated by Django 3.1.2 on 2020-10-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_device_device_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='confirmation_code',
            field=models.CharField(default='NPSRE', max_length=5),
        ),
    ]
