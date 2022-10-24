from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ContactPerson, Location, School
from .serializers import SchoolSerializer, LocationSerializer, ContactPersonSerializer, SchoolSerializer_NO_ID
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Schools(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer_NO_ID


class SchoolDetail(RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
