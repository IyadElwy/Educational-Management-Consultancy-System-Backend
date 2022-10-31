from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import School
from .serializers import SchoolSerializer, SchoolSerializer_NO_ID
from django_filters.rest_framework import DjangoFilterBackend


class Schools(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'is_activated', 'location']


class SchoolDetail(RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
