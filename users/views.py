from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import VolunteerSerializer, UserSerializer
from .models import User
import json

# Create your views here.

class RegisterVolunteerView(APIView):
    def post(self, request):
        data = request.data
        userinfo = data['user']
        userinfo['is_Volunteer'] = True
        Userializer = UserSerializer(data=userinfo)
        Userializer.is_valid(raise_exception=True)

        user =  Userializer.save()
        volunteerinfo = data['volunteer']

        volunteerinfo['user'] = user.id
        Volunteerializer = VolunteerSerializer(data=volunteerinfo)
        Volunteerializer.is_valid(raise_exception=True)
        Volunteerializer.save()

        return Response(Userializer.data);
