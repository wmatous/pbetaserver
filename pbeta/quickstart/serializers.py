from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pbeta.quickstart.models import (Forecast, Trip, Attribute)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ForecastSerializer(serializers.HyperlinkedModelSerializer):

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(ForecastSerializer, self).run_validators(value)

    def create(self, validated_data):
        instance, _ = Forecast.objects.get_or_create(**validated_data)
        return instance

    class Meta:
        model = Forecast
        fields = ('url', 'id', 'forecast_url') 

class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(AttributeSerializer, self).run_validators(value)

    def create(self, validated_data):
        instance, _ = Attribute.objects.get_or_create(**validated_data)
        return instance
    
    class Meta:        
        model = Attribute
        fields = ('url', 'id','name', 'badge')

class TripSerializer(serializers.HyperlinkedModelSerializer):
    # forecasts = ForecastSerializer()
    class Meta:
        model = Trip
        fields = ('url', 'id', 'latitude', 'longitude', 'title', 'duration','distance', 'description' , 'forecasts', 'attributes')

