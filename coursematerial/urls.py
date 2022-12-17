from django.urls import path
from .views import SchoolMaterials, SchoolMaterialDetail

urlpatterns = [
    path('school/', SchoolMaterials.as_view()),
    path('school/<int:pk>/', SchoolMaterialDetail.as_view()),
]
