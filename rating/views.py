from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MLScoreSerializer_NO_ID, MLScoreSerializer, StudentRatingSerializer, \
    StudentRatingSerializer_NO_ID, CoordinatorRatingSerializer, CoordinatorRatingSerializer_NO_ID
from .models import CoordinatorRating, StudentRating, MLScore


class CoordinatorRatings(ListCreateAPIView):
    queryset = CoordinatorRating.objects.all()
    serializer_class = CoordinatorRatingSerializer_NO_ID


class CoordinatorRatingDetail(RetrieveUpdateDestroyAPIView):
    queryset = CoordinatorRating.objects.all()
    serializer_class = CoordinatorRatingSerializer


class StudentRatings(ListCreateAPIView):
    queryset = StudentRating.objects.all()
    serializer_class = StudentRatingSerializer_NO_ID


class StudentRatingDetail(RetrieveUpdateDestroyAPIView):
    queryset = StudentRating.objects.all()
    serializer_class = StudentRatingSerializer


class MLScores(ListCreateAPIView):
    queryset = MLScore.objects.all()
    serializer_class = MLScoreSerializer


class MLScoreDetail(RetrieveUpdateDestroyAPIView):
    queryset = MLScore.objects.all()
    serializer_class = MLScoreSerializer_NO_ID
