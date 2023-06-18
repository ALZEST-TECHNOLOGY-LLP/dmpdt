# Generated by Django 4.1.7 on 2023-03-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_data',
            old_name='vehicle_id',
            new_name='device_id',
        ),
        migrations.AddField(
            model_name='user_data',
            name='vehicle_number',
            field=models.CharField(default=1, max_length=65, verbose_name=''),
            preserve_default=False,
        ),
    ]