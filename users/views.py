from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import VolunteerSerializer, UserSerializer, StudentSerializer, AdminSerializer, School_AdminSerializer
from .models import User, Volunteer, Student, Admin, School_Admin
import jwt, datetime
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


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(username=email).first()

        # Exception Handling
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        #Generating Payload for JWT

        role = ''
        if user.is_Volunteer:
            role = 'Volunteer'
        if user.is_Student:
            role = 'Student'
        if user.is_Admin:
            role = 'Admin'
        if user.is_School_Admin:
            role = 'School_Admin'

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            'role': role
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        extra = {}
        serializer1 = None
        if user.is_Volunteer:
            volunteer = Volunteer.objects.filter(user=user).first()
            serializer1 = VolunteerSerializer(volunteer)
        if user.is_Student:
            student = Student.objects.filter(user=user).first()
            serializer1 = StudentSerializer(student)
        if user.is_Admin:
            admin = Admin.objects.filter(user=user).first()
            serializer1 = AdminSerializer(admin)
        if user.is_School_Admin:
            school_admin = School_Admin.objects.filter(user=user).first()
            serializer1 = School_AdminSerializer(school_admin)

        extra['user'] = serializer.data
        extra['extra'] = serializer1.data
        return Response(extra)
