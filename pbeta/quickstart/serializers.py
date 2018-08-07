from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pbeta.quickstart.models import (Forecast, Trip)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forecast
        fields = ('id', 'one_day' , 'three_day', 'six_day' ,  'one_day_r' , 'three_day_r',  'six_day_r') 


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'latitude', 'longitude', 'name', 'duration','distance', 'forecast_url', 'forecast')