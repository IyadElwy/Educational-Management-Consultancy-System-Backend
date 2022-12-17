import json
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MLScoreSerializer_NO_ID, MLScoreSerializer, StudentRatingSerializer, \
    StudentRatingSerializer_NO_ID, CoordinatorRatingSerializer, CoordinatorRatingSerializer_NO_ID
from .models import CoordinatorRating, StudentRating, MLScore
from session import models as session_model
from rest_framework.response import Response
from django.core import serializers


class CoordinatorRatings(ListCreateAPIView):
    serializer_class = CoordinatorRatingSerializer_NO_ID

    def get_queryset(self):
        qs = CoordinatorRating.objects.filter(session=self.kwargs['pk'])
        return qs

    def create(self, request, *args, **kwargs):
        rating = CoordinatorRating.objects.create(question_1=dict(request.POST)['question_1'][0],
                                                  question_2=dict(request.POST)['question_2'][0],
                                                  question_3=dict(request.POST)['question_3'][0],
                                                  question_4=dict(request.POST)['question_4'][0],
                                                  question_5=dict(request.POST)['question_5'][0],
                                                  question_6=dict(request.POST)['question_6'][0],
                                                  session=session_model.Session.objects.get(id=self.kwargs['pk'])
                                                  )

        return Response(json.loads(serializers.serialize('json', [rating])))


class CoordinatorRatingDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CoordinatorRatingSerializer
    queryset = StudentRating.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            rating = CoordinatorRating.objects.get(id=self.kwargs['ratingid'])
            return Response(json.loads(serializers.serialize('json', [rating])))
        except Exception as e:
            return Response([])


class StudentRatings(ListCreateAPIView):
    serializer_class = StudentRatingSerializer_NO_ID

    def get_queryset(self):
        qs = StudentRating.objects.filter(session=self.kwargs['pk'])
        return qs

    def create(self, request, *args, **kwargs):
        rating = StudentRating.objects.create(question_1=dict(request.POST)['question_1'][0],
                                              question_2=dict(request.POST)['question_2'][0],
                                              question_3=dict(request.POST)['question_3'][0],
                                              question_4=dict(request.POST)['question_4'][0],
                                              question_5=dict(request.POST)['question_5'][0],
                                              question_6=dict(request.POST)['question_6'][0],
                                              question_7=dict(request.POST)['question_7'][0],
                                              question_8=dict(request.POST)['question_8'][0],
                                              question_9=dict(request.POST)['question_9'][0],
                                              question_10=dict(request.POST)['question_10'][0],
                                              question_11=dict(request.POST)['question_11'][0],
                                              session=session_model.Session.objects.get(id=self.kwargs['pk'])
                                              )

        return Response(json.loads(serializers.serialize('json', [rating])))


class StudentRatingDetail(RetrieveUpdateDestroyAPIView):
    queryset = StudentRating.objects.all()
    serializer_class = StudentRatingSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            rating = StudentRating.objects.get(id=self.kwargs['ratingid'])
            return Response(json.loads(serializers.serialize('json', [rating])))
        except Exception as e:
            return Response([])


class MLScores(ListCreateAPIView):
    serializer_class = MLScoreSerializer_NO_ID

    def get_queryset(self):
        qs = MLScore.objects.filter(session=self.kwargs['pk'])
        return qs

    def create(self, request, *args, **kwargs):
        rating = MLScore.objects.create(percentage=dict(request.POST)['percentage'][0],
                                        session=session_model.Session.objects.get(id=self.kwargs['pk'])
                                        )
        return Response(json.loads(serializers.serialize('json', [rating])))


class MLScoreDetail(RetrieveUpdateDestroyAPIView):
    queryset = MLScore.objects.all()
    serializer_class = MLScoreSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            rating = MLScore.objects.get(id=self.kwargs['ratingid'])
            return Response(json.loads(serializers.serialize('json', [rating])))
        except Exception as e:
            return Response([])
