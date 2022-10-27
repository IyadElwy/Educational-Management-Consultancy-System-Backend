from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SessionSerializer_NO_ID, SessionSerializer
from .models import Session


class Sessions(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer_NO_ID


class SessionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
