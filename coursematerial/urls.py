from django.urls import path
from .views import SchoolMaterials, VolunteerMaterials, SchoolMaterialDetail, VolunteerMaterials

urlpatterns = [
    path('school/', SchoolMaterials.as_view()),
    path('volunteer/', VolunteerMaterials.as_view()),
    path('school/<int:pk>/', SchoolMaterialDetail.as_view()),
    path('volunteer/<int:pk>/', VolunteerMaterials.as_view()),
]
