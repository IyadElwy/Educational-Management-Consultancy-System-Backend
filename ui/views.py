from django.shortcuts import render
from django.conf import settings


def home(req):
    return render(request=req, template_name='home.html')


def login(req):
    return render(request=req, template_name='login.html')


def register_school(req):
    return render(request=req, template_name='register_school.html',
                  context={'key': settings.GCP_API})


def register_volunteer(req):
    return render(request=req, template_name='register_volunteer.html')


def download_app(req):
    return render(request=req, template_name='download_our_app.html')


##############################################################################

def admin_home(req):
    return render(request=req, template_name='admin_home.html')


def admin_schools(req):
    return render(request=req, template_name='admin_schools.html')


def admin_views_single_school(req, schoolid):
    return render(request=req, template_name='admin_view_single_school.html')


def admin_volunteers(req):
    return render(request=req, template_name='admin_volunteers.html')


def admin_views_single_volunteer(req, volunteerid):
    return render(request=req, template_name='admin_views_single_volunteer.html')


def admin_upcoming_sessions(req):
    return render(request=req, template_name='admin_upcoming_sessions.html')


def admin_views_single_upcoming_session(req, sessionid):
    return render(request=req, template_name='admin_views_single_upcoming_session.html')


def admin_past_sessions(req):
    return render(request=req, template_name='admin_past_sessions.html')


def admin_views_single_past_session(req, sessionid):
    return render(request=req, template_name='admin_views_single_past_session.html')


##############################################################################

def school_admin_home(req):
    return render(request=req, template_name='school_admin_home.html')


def school_admin_upcoming_sessions(req):
    return render(request=req, template_name='school_admin_upcoming_sessions.html')


def school_admin_views_single_upcoming_session(req, sessionid):
    return render(request=req, template_name='school_admin_views_single_upcoming_session.html')


def school_admin_past_sessions(req):
    return render(request=req, template_name='school_admin_past_sessions.html')


def school_admin_views_single_past_session(req, sessionid):
    return render(request=req, template_name='school_admin_views_single_past_session.html')


def school_admin_add_session(req):
    return render(request=req, template_name='school_admin_add_session.html')


def school_admin_courses(req):
    return render(request=req, template_name='school_admin_courses.html')


def school_admin_views_single_course(req, courseid):
    return render(request=req, template_name='school_admin_views_single_course.html')


##############################################################################
def error_404_handler(req, exception):
    return render(request=req, template_name='404.html')
