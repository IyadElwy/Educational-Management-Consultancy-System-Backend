from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SchoolMaterialSerializer, VolunteerMaterialSerializer, SchoolMaterialSerializer_NO_ID, \
    VolunteerMaterialSerializer_NO_ID
from .models import SchoolMaterial, VolunteerMaterial


class SchoolMaterials(ListCreateAPIView):
    queryset = SchoolMaterial.objects.all()
    serializer_class = SchoolMaterialSerializer_NO_ID


class SchoolMaterialDetail(RetrieveUpdateDestroyAPIView):
    queryset = SchoolMaterial.objects.all()
    serializer_class = SchoolMaterialSerializer


class VolunteerMaterials(ListCreateAPIView):
    queryset = VolunteerMaterial.objects.all()
    serializer_class = VolunteerMaterialSerializer_NO_ID


class VolunteerMaterialDetail(RetrieveUpdateDestroyAPIView):
    queryset = VolunteerMaterial.objects.all()
    serializer_class = VolunteerMaterialSerializer
