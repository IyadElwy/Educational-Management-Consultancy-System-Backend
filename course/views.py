from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CourseSerializer_NO_ID, CourseSerializer
from .models import Course


class Courses(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer_NO_ID


class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
