from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import School
from .serializers import SchoolSerializer, SchoolSerializer_NO_ID


class Schools(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer_NO_ID


class SchoolDetail(RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
