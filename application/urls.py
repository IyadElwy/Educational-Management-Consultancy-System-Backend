from django.urls import path
from .views import Applications, ApplicationDetail

urlpatterns = [
    path('', Applications.as_view()),
    path('<int:pk>/', ApplicationDetail.as_view())
]
