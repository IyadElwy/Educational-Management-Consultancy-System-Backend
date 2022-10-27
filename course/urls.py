from django.urls import path
from .views import Courses, CourseDetail

urlpatterns = [
    path('', Courses.as_view()),
    path('<int:pk>/', CourseDetail.as_view())
]
