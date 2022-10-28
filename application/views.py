from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ApplicationSerializer, ApplicationSerializer_NO_ID
from .models import Application


class Applications(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer_NO_ID


class ApplicationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
