from django.conf import settings
import io
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
import datetime

import users.models
from session.models import Session
from .forms import AddMaterialForm, AddCourseForm
from coursematerial import models as material_models
from course import models as course_models
from session import models as session_models
from school import models as school_models
from rating import models as rating_models
from utils import gcp_functions
from django.views.generic import CreateView
from django.views import generic
from users import models as user_models


def home(req):
    return render(request=req, template_name='home.html')


def register_volunteer(req):
    return render(request=req, template_name='register_volunteer.html')


def download_app(req):
    return render(request=req, template_name='download_our_app.html')


##############################################################################

def admin_home(req):
    return render(request=req, template_name='admin_home.html')


def admin_schools(req):
    schools = school_models.School.objects.all()
    return render(request=req, template_name='admin_schools.html', context={'schools': schools})


def admin_views_single_school(req, schoolid):
    school = school_models.School.objects.get(id=schoolid)
    return render(request=req, template_name='admin_view_single_school.html', context={'school': school})


def admin_volunteers(req):
    return render(request=req, template_name='admin_volunteers.html')


def admin_views_single_volunteer(req, volunteerid):
    return render(request=req, template_name='admin_views_single_volunteer.html')


def admin_upcoming_sessions(req):
    sessions = session_models.Session.objects.filter(start_time__gt=datetime.datetime.now())
    return render(request=req, template_name='admin_upcoming_sessions.html', context={'sessions': sessions})


def admin_views_single_upcoming_session(req, sessionid):
    session = session_models.Session.objects.get(id=sessionid)
    return render(request=req, template_name='admin_views_single_upcoming_session.html', context={'session': session})


def admin_past_sessions(req):
    sessions = session_models.Session.objects.filter(end_time__lt=datetime.datetime.now())
    return render(request=req, template_name='admin_past_sessions.html', context={'sessions': sessions})


def admin_views_single_past_session(req, sessionid):
    session = session_models.Session.objects.get(id=sessionid)
    return render(request=req, template_name='admin_views_single_past_session.html', context={'session': session})


##############################################################################

def school_admin_home(req, pk):
    return render(request=req, template_name='school_admin_home.html', context={'school':
                                                                                    school_models.School.objects.filter(
                                                                                        school_admin=user_models.School_Admin.objects.get(
                                                                                            user=req.user))[0]})


def school_admin_upcoming_sessions(req):
    sessions = session_models.Session.objects.filter(start_time__gt=datetime.datetime.now())
    return render(request=req, template_name='school_admin_upcoming_sessions.html', context={'sessions': sessions})


def school_admin_views_single_upcoming_session(req, sessionid):
    return render(request=req, template_name='school_admin_views_single_upcoming_session.html')


def school_admin_past_sessions(req):
    sessions = session_models.Session.objects.filter(end_time__lt=datetime.datetime.now())
    return render(request=req, template_name='school_admin_past_sessions.html', context={'sessions': sessions})


class school_admin_views_single_past_session(CreateView):
    model = rating_models.CoordinatorRating
    template_name = 'school_admin_views_single_past_session.html'
    fields = (
        'question_1',
        'question_2',
        'question_3',
        'question_4',
        'question_5',
        'question_6',
    )

    def form_valid(self, form):
        form.instance.session = session_models.Session.objects.get(id=self.kwargs['sessionid'])
        return super(school_admin_views_single_past_session, self).form_valid(form)

    def get_success_url(self):
        rating_models.Rating.objects.create(CoordinatorRating_id=self.object.id)
        return reverse('school_admin_views_past_sessions')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['session'] = session_models.Session.objects.get(id=self.kwargs['sessionid'])
        return data


class school_admin_add_session(CreateView):
    model = Session
    template_name = 'school_admin_add_session.html'
    fields = (
        'course',
        'description',
        'start_time',
        'end_time',
    )
    success_url = reverse_lazy('school_admin_views_upcoming_sessions')


def school_admin_courses(req):
    if req.method == 'POST':
        form = AddCourseForm(req.POST, req.FILES)
        if form.is_valid():
            school = \
                school_models.School.objects.filter(school_admin=user_models.School_Admin(user_id=req.user.pk))[0]

            return render(req, 'school_admin_courses.html', {'form': form, 'courses': course_models.Course.objects.all(
            ).filter(school=school)})
    else:
        form = AddCourseForm()

        school = \
            school_models.School.objects.filter(school_admin=user_models.School_Admin(user_id=req.user.pk))[0]

        return render(req, 'school_admin_courses.html', {'form': form, 'courses': course_models.Course.objects.all(
        ).filter(school=school)})


def admin_add_course(req):
    if req.method == 'POST':
        school = None
        form = AddCourseForm(req.POST, req.FILES)
        if form.is_valid():
            material_name = dict(req.POST)['name'][0]
            description = dict(req.POST)['description'][0]
            grade_level = int(dict(req.POST)['grade_level'][0])
            school = \
                school_models.School.objects.filter(school_admin=user_models.School_Admin(user_id=req.user.pk))[0]
            course_models.Course.objects.create(name=material_name, description=description, grade_level=grade_level,
                                                school=school)
            return render(req, 'school_admin_courses.html', {'form': form, 'courses': course_models.Course.objects.all(
            ).filter(school=school)})
        else:
            form = AddCourseForm()

        school = \
            school_models.School.objects.filter(school_admin=user_models.School_Admin(user_id=req.user.pk))[0]
        return render(req, 'school_admin_courses.html', {'form': form, 'courses': course_models.Course.objects.all(
        ).filter(school=school)})


def school_admin_views_single_course(req, courseid):
    course = course_models.Course.objects.get(id=courseid)

    material = material_models.SchoolMaterial.objects.all().filter(course=course)
    if req.method == 'POST':
        form = AddMaterialForm(req.POST, req.FILES)
        if form.is_valid():
            return render(req, 'school_admin_views_single_course.html',
                          {'form': form, 'course': course, 'material': material})
    else:
        form = AddMaterialForm()

    return render(req, 'school_admin_views_single_course.html', {'form': form, 'course': course, 'material': material})


def SchoolMaterialDownload(req, courseid, materialid):
    file_obj = io.BytesIO()
    file_obj = gcp_functions.download_blob(settings.BUCKET_NAME, f'material_{materialid}.pdf')
    response = HttpResponse(file_obj, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=material_{materialid}.pdf'

    return response


def schoolMaterialUpload(req, courseid):
    course = course_models.Course.objects.get(id=courseid)

    material = material_models.SchoolMaterial.objects.all().filter(course=course)

    if req.method == 'POST':
        new_material = material_models.SchoolMaterial.objects.create(name=dict(req.POST)['material_name'][0],
                                                                     course=course,
                                                                     description='',
                                                                     uploaded_by=user_models.School_Admin.objects.get(
                                                                         user=req.user.pk))

        gcp_functions.upload_blob_from_memory(settings.BUCKET_NAME,
                                              dict(req.FILES)['material_file'][0].file.getvalue(),
                                              f'material_{new_material.pk}.pdf')

        form = AddMaterialForm(req.POST, req.FILES)
        if form.is_valid():
            return render(req, 'school_admin_views_single_course.html',
                          {'form': form, 'course': course, 'material': material})
    else:
        form = AddMaterialForm()

    return render(req, 'school_admin_views_single_course.html', {'form': form, 'course': course, 'material': material})


##############################################################################
def error_404_handler(req, exception):
    return render(request=req, template_name='404.html')

##############################################################################
