# Generated by Django 3.1.2 on 2020-12-04 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='device',
        ),
    ]