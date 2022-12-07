from django.shortcuts import render


def home(req):
    return render(request=req, template_name='home.html')


def login(req):
    return render(request=req, template_name='login.html')


def register_school(req):
    return render(request=req, template_name='')


def register_volunteer(req):
    return render(request=req, template_name='')


def download_app(req):
    return render(request=req, template_name='download_our_app.html')


##############################################################################

def admin_home(req):
    return render(request=req, template_name='admin_dashboard.html')


def admin_schools(req):
    return render(request=req, template_name='admin_schools.html')


def admin_views_single_school(req):
    return render(request=req, template_name='')


def admin_volunteers(req):
    return render(request=req, template_name='admin_volunteers.html')


def admin_views_single_volunteer(req):
    return render(request=req, template_name='')


def admin_upcoming_sessions(req):
    return render(request=req, template_name='admin_upcoming_sessions.html')


def admin_views_single_upcoming_session(req):
    return render(request=req, template_name='')


def admin_past_sessions(req):
    return render(request=req, template_name='admin_past_sessions.html')


def admin_views_single_past_session(req):
    return render(request=req, template_name='')


##############################################################################

def school_admin_home(req):
    return render(request=req, template_name='school_admin_dashboard.html')


def school_admin_upcoming_sessions(req):
    return render(request=req, template_name='school_admin_upcoming_sessions.html')


def school_admin_views_single_upcoming_session(req):
    return render(request=req, template_name='')


def school_admin_views_single_upcoming_session_applications(req):
    return render(request=req, template_name='')


def school_admin_views_single_application_from_upcoming_session(req):
    return render(request=req, template_name='')


def school_admin_past_sessions(req):
    return render(request=req, template_name='school_admin_past_sessions.html')


def school_admin_views_single_past_session(req):
    return render(request=req, template_name='')


def school_admin_add_session(req):
    return render(request=req, template_name='school_admin_add_session.html')


def school_admin_courses(req):
    return render(request=req, template_name='school_admin_courses.html')


def school_admin_views_single_course(req):
    return render(request=req, template_name='')


def school_admin_add_course(req):
    return render(request=req, template_name='school_admin_add_courses.html')

##############################################################################
