# Generated by Django 4.1.7 on 2023-03-31 08:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_remove_vehicle_details_user_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vehicle_details',
            new_name='deviced',
        ),
    ]