# Generated by Django 5.0.4 on 2024-04-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingstation',
            name='brand',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='chargingstation',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='chargingstation',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
    ]