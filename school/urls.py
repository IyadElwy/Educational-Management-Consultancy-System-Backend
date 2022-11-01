from django.urls import path
from .views import Schools, SchoolDetail, Locations, LocationDetail

urlpatterns = [
    path('', Schools.as_view()),
    path('<int:pk>/', SchoolDetail.as_view()),
    path('locations/', Locations.as_view()),
    path('locations/<int:pk>/', LocationDetail.as_view())
]
