from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from session.models import Session
from application.models import Application
from .models import Volunteer,Student,Admin,School_Admin,User
from rest_framework.exceptions import AuthenticationFailed
import jwt
@api_view(['GET'])
def getMySessions(request):

    # Validate the token and make sure it's a volunteer
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    if not user.is_Volunteer:
        raise AuthenticationFailed('Unauthenticated!')
    if payload['role'] != 'Volunteer':
        raise AuthenticationFailed('Cannot Take Classes!')

    volunteer = Volunteer.objects.filter(user=user).first()

    # After Authenticating that this is truly a volunteer, we can get the sessions

    sessions = Session.objects.filter(taught_by=volunteer)
    courses = []
    for session in sessions:
        # courses.append({'name':session.session.course.name,'id':session.session.id,'School':session.session.course.name})
        courses.append({'id': session.session.id, 'name': session.session.course.name,
                        'location': 'Empty Place holder value add after migration', 'date': session.session.start_time,
                        'description': session.session.description, 'school_name': session.session.course.school.name,
                        'school_id': session.session.course.school.id, 'taught_by': session.session.taught_by})
    return Response(courses)
@api_view(['POST'])
def applyToSession(request):

    # Validate the token and make sure it's a volunteer
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    if not user.is_Volunteer:
        raise AuthenticationFailed('Unauthenticated!')
    if payload['role'] != 'Volunteer':
        raise AuthenticationFailed('Unauthenticated!')

    volunteer = Volunteer.objects.filter(user=user).first()

    if volunteer.status != 'Accepted':
        raise AuthenticationFailed('You are not accepted yet!')

    # After Authenticating that this is truly a volunteer and that he is accepted, we can now perform logic checks to ensure the volunteer can apply to the session

    session_id = request.data['session_id']
    session = Session.objects.filter(id=session_id).first()


    if not session:
        raise AuthenticationFailed('Invalid session!')

    app = Application.objects.filter(volunteer=volunteer, session=session)

    if app:
        raise AuthenticationFailed('You have already applied to this session!')

    # Create the application

    Application.objects.create(volunteer=volunteer, session=session)


    return Response('Applied successfully!')


@api_view(['GET'])
def getMyPendingSessions(request):
    # Validate the token and make sure it's a volunteer
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    if not user.is_Volunteer:
        raise AuthenticationFailed('Unauthenticated!')
    if payload['role'] != 'Volunteer':
        raise AuthenticationFailed('Unauthenticated!')

    volunteer = Volunteer.objects.filter(user=user).first()

    # After Authenticating that this is truly a volunteer, we can get the sessions that are pending

    sessions = Application.objects.filter(volunteer=volunteer, status='In Process')
    courses = []
    for session in sessions:
        courses.append({'id': session.session.id, 'name': session.session.course.name,
                        'location': 'Empty Place holder value add after migration', 'date': session.session.start_time,
                        'description': session.session.description, 'school_name': session.session.course.school.name,
                        'school_id': session.session.course.school.id, 'taught_by': session.session.taught_by})
    return Response(courses)