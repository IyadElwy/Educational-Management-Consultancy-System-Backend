from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import VolunteerSerializer, UserSerializer, StudentSerializer, AdminSerializer, School_AdminSerializer
from .models import User
import json

# Create your views here.

class RegisterVolunteerView(APIView):
    def post(self, request):
        data = request.data
        userinfo = data['user']
        userinfo['is_Volunteer'] = True
        print(userinfo)
        Userializer = UserSerializer(data=userinfo)
        Userializer.is_valid(raise_exception=True)
        user =  Userializer.save()
        volunteerinfo = data['volunteer']

        volunteerinfo['user'] = user.id
        Volunteerializer = VolunteerSerializer(data=volunteerinfo)
        Volunteerializer.is_valid(raise_exception=True)
        Volunteerializer.save()

        return Response(Userializer.data);

class RegisterStudentView(APIView):
    def post(self, request):
        data = request.data
        userinfo = data['user']
        userinfo['is_Student'] = True
        Userializer = UserSerializer(data=userinfo)
        Userializer.is_valid(raise_exception=True)

        user = Userializer.save()
        studentinfo = data['student']

        studentinfo['user'] = user.id
        studentSerializer = StudentSerializer(data=studentinfo)
        studentSerializer.is_valid(raise_exception=True)
        studentSerializer.save()

        return Response(Userializer.data)

class RegisterAdminView(APIView):
    def post(self, request):
        data = request.data
        userinfo = data['user']
        userinfo['is_Admin'] = True
        Userializer = UserSerializer(data=userinfo)
        Userializer.is_valid(raise_exception=True)

        user = Userializer.save()
        admininfo={}

        admininfo['user']=user.id
        adminSerializers = AdminSerializer(data=admininfo)
        adminSerializers.is_valid(raise_exception=True)
        adminSerializers.save()

        return Response(Userializer.data);


class RegisterSchoolAdminView(APIView):
    def post(self, request):
        data = request.data
        userinfo = data['user']
        userinfo['is_School_Admin'] = True
        Userializer = UserSerializer(data=userinfo)
        Userializer.is_valid(raise_exception=True)

        user = Userializer.save()
        admininfo = {}

        admininfo['user'] = user.id
        adminSerializers = School_AdminSerializer(data=admininfo)
        adminSerializers.is_valid(raise_exception=True)
        adminSerializers.save()

        return Response(Userializer.data)