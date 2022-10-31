from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SchoolMaterialSerializer, VolunteerMaterialSerializer, SchoolMaterialSerializer_NO_ID, \
    VolunteerMaterialSerializer_NO_ID
from .models import SchoolMaterial, VolunteerMaterial
from django_filters.rest_framework import DjangoFilterBackend


class SchoolMaterials(ListCreateAPIView):
    queryset = SchoolMaterial.objects.all()
    serializer_class = SchoolMaterialSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class SchoolMaterialDetail(RetrieveUpdateDestroyAPIView):
    queryset = SchoolMaterial.objects.all()
    serializer_class = SchoolMaterialSerializer


class VolunteerMaterials(ListCreateAPIView):
    queryset = VolunteerMaterial.objects.all()
    serializer_class = VolunteerMaterialSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'is_public']


class VolunteerMaterialDetail(RetrieveUpdateDestroyAPIView):
    queryset = VolunteerMaterial.objects.all()
    serializer_class = VolunteerMaterialSerializer
