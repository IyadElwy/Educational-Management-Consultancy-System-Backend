from django.urls import path, re_path
from .views import Courses, CourseDetail

urlpatterns = [
    path('', Courses.as_view()),
    path('<int:pk>/', CourseDetail.as_view())
]
