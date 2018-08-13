# Generated by Django 2.0.7 on 2018-08-08 07:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_auto_20180808_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='trip',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='forecast_url',
            field=models.URLField(primary_key=True),
        ),
    ]
