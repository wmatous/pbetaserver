from django.db.models import ( Model, CharField, PositiveSmallIntegerField, DecimalField, DurationField, URLField)



# Create your models here.

class Forecast(Model):
    one_day = PositiveSmallIntegerField()  
    three_day = PositiveSmallIntegerField()  
    six_day = PositiveSmallIntegerField()  
    one_day_r = PositiveSmallIntegerField()  
    three_day_r = PositiveSmallIntegerField()  
    six_day_r = PositiveSmallIntegerField()  

class Trip(Model):
    name = CharField(max_length=255)
    distance = DecimalField(max_digits=9, decimal_places=2)
    duration = DurationField()
    forecast_url = URLField(max_length=200)
    forecast = Forecast()

 
