from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User, Group
from pbeta.quickstart.models import Trip, Forecast
from rest_framework import viewsets
from pbeta.quickstart.serializers import UserSerializer, GroupSerializer, TripSerializer, ForecastSerializer

def home(request):
	return render(request, 'home.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TripViewSet(viewsets.ModelViewSet):

    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class ForecastSerializer(viewsets.ModelViewSet):

    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer