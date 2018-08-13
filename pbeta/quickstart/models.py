from django.db.models import ( Model, CharField, PositiveSmallIntegerField, DecimalField, DurationField, 
URLField, UUIDField, ManyToManyField, TextField)
import uuid


# Create your models here.

class Forecast(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    forecast_url = URLField(max_length=200)
    one_day = PositiveSmallIntegerField(null = True)  
    three_day = PositiveSmallIntegerField(null = True)  
    six_day = PositiveSmallIntegerField(null = True)  
    one_day_r = PositiveSmallIntegerField(null = True)  
    three_day_r = PositiveSmallIntegerField(null = True)  
    six_day_r = PositiveSmallIntegerField(null = True)  

class Trip(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=255)
    description = TextField(blank=True)
    attributes = ManyToManyField('Attribute', blank=True)
    distance = DecimalField(max_digits=9, decimal_places=2, null = True)
    duration = DurationField(null = True)
    latitude = DecimalField(max_digits=9, decimal_places=6,  null = True)
    longitude = DecimalField(max_digits=9, decimal_places=6, null = True)
    # forecast_url = URLField(max_length=200,  null = True)
    forecasts = ManyToManyField('Forecast', blank=True)

class Attribute(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    badge = CharField(max_length=255)

 
