from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls import handler404

#####################################################################################################

urlpatterns = [
    #####################################################################################################
    # general
    path('', views.home, name='homepage'),
    # path('registerschool/', views.register_school.as_view(), name='register_school'),
    # path('registervolunteer/', views.register_volunteer, name='register_volunteer'),
    path('downloadapp/', views.download_app, name='download_app'),
    #####################################################################################################
    # admin
    path('admin/', views.admin_home, name='admin_homepage'),
    path('admin/schools/', views.admin_schools, name='admin_views_school'),
    path('admin/schools/<int:schoolid>/', views.admin_views_single_school, name='admin_views_single_school'),
    path('admin/volunteers/', views.admin_volunteers, name='admin_views_volunteers'),
    path('admin/volunteers/<int:volunteerid>/', views.admin_views_single_volunteer,
         name='admin_views_single_volunteer'),
    path('admin/upcomingsessions/', views.admin_upcoming_sessions, name='admin_views_upcoming_sessions'),
    path('admin/upcomingsessions/<int:sessionid>/', views.admin_views_single_upcoming_session,
         name='admin_views_single_upcoming_session'),
    path('admin/pastsessions/', views.admin_past_sessions, name='admin_views_past_sessions'),
    path('admin/pastsessions/<int:sessionid>/', views.admin_views_single_past_session,
         name='admin_views_single_past_session'),
    #######################################################################################################
    # school admin
    path('schooladmin/<int:pk>', views.school_admin_home, name='school_admin_homepage'),
    path('schooladmin/upcomingsessions/', views.school_admin_upcoming_sessions,
         name='school_admin_views_upcoming_sessions'),
    path('schooladmin/upcomingsessions/<int:sessionid>/', views.school_admin_views_single_upcoming_session,
         name='school_admin_views_single_upcoming_session'),
    path('schooladmin/pastsessions/', views.school_admin_past_sessions, name='school_admin_views_past_sessions'),
    path('schooladmin/pastsessions/<int:sessionid>/', views.school_admin_views_single_past_session.as_view(),
         name='school_admin_views_single_past_session'),
    path('schooladmin/courses', views.school_admin_courses, name='school_admin_views_courses'),
    path('schooladmin/courses/<int:courseid>/', views.school_admin_views_single_course,
         name='school_admin_views_single_course'),
    path('schooladmin/addsession', views.school_admin_add_session.as_view(), name='school_admin_addsession`'),
    path('schooladmin/courses/<int:courseid>/material/upload', views.schoolMaterialUpload,
         name='school_admin_upload_material'),
    path('schooladmin/courses/<int:courseid>/material/<int:materialid>/', views.SchoolMaterialDownload,
         name='school_admin_download_material'),
    path('schooladmin/courses/addcourse', views.admin_add_course,
         name='school_admin_add_course'),

    #####################################################################################################
    path('accounts/login/', include('django.contrib.auth.urls')),
]

#####################################################################################################

handler404 = 'ui.views.error_404_handler'
