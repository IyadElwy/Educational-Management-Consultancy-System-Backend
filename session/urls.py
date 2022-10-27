from django.urls import path
from .views import Sessions, SessionDetail

urlpatterns = [
    path('', Sessions.as_view()),
    path('<int:pk>/', SessionDetail.as_view())
]
