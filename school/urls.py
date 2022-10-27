from django.urls import path
from .views import Schools, SchoolDetail

urlpatterns = [
    path('', Schools.as_view()),
    path('/<int:pk>/', SchoolDetail.as_view())
]
