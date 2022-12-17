from django.urls import path
from .views import SchoolMaterials, SchoolMaterialDetail

urlpatterns = [
    path('school/<int:schoolid>/course/<int:courseid>', SchoolMaterials.as_view()),
    # path('school/<int:schoolid>/course/<int:courseid>/', SchoolMaterialDetail.as_view()),
]
