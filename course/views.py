from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CourseSerializer_NO_ID, CourseSerializer
from .models import Course
from django_filters.rest_framework import DjangoFilterBackend


class Courses(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school', 'grade_level', 'name']


class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
