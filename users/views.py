from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import VolunteerSerializer
from .models import User
# Create your views here.

class RegisterVolunteerView(APIView):
    def post(self, request):
        serializer = VolunteerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data);
