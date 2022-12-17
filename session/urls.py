from django.urls import path
from .views import Sessions, SessionDetail
from rating import views as rating_views

urlpatterns = [
    path('', Sessions.as_view()),
    path('<int:pk>/', SessionDetail.as_view()),
    path('<int:pk>/coordinatorrating/', rating_views.CoordinatorRatings.as_view()),
    path('<int:pk>/coordinatorrating/<int:ratingid>/', rating_views.CoordinatorRatingDetail.as_view()),
    path('<int:pk>/studentrating/', rating_views.StudentRatings.as_view()),
    path('<int:pk>/studentrating/<int:ratingid>/', rating_views.StudentRatingDetail.as_view()),
    path('<int:pk>/mlrating/', rating_views.MLScores.as_view()),
    path('<int:pk>/mlrating/<int:ratingid>/', rating_views.MLScoreDetail.as_view()),
]
