from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import School, Location
from .serializers import SchoolSerializer, SchoolSerializer_NO_ID, LocationSerializer_NO_ID, LocationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class Schools(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'is_activated', 'location']


class SchoolDetail(RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class Locations(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'city', 'district']


class LocationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
