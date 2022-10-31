from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SessionSerializer_NO_ID, SessionSerializer
from .models import Session
from django_filters.rest_framework import DjangoFilterBackend


class Sessions(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer_NO_ID
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'start_time', 'end_time']


class SessionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
