# Generated by Django 2.0.7 on 2018-08-07 01:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20180807_0108'),
    ]



    operations = [
        migrations.RunSQL(


        ),
        migrations.AddField(
            model_name='trip',
            name='forecasts',
            field=models.ManyToManyField(to='quickstart.Forecast'),
        ),
        migrations.RemoveField(
            model_name='forecast',
            name='id',
            ),
        migrations.RemoveField(
            model_name='trip',
            name='id',
            ),
    ]
