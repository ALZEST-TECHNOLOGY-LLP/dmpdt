# Generated by Django 4.1.7 on 2023-03-30 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_sensordata_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle_details',
            name='last_login_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
