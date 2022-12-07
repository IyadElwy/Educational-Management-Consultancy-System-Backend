from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('registerschool/', views.register_school),
    path('registervolunteer/', views.register_volunteer),
    path('downloadapp/', views.download_app),
    #####################################################################################################
    path('admin/', views.admin_home),
    path('admin/schools/', views.admin_schools),
    path('admin/schools/<pk:int>/', views.admin_views_single_school),
    path('admin/volunteers/', views.admin_volunteers),
    path('admin/volunteers/<pk:int>/', views.admin_views_single_volunteer),
    path('admin/upcomingsessions/', views.admin_upcoming_sessions),
    path('admin/upcomingsessions/<pk:int>/', views.admin_views_single_upcoming_session),
    path('admin/pastsessions/', views.admin_past_sessions),
    path('admin/pastsessions/<pk:int>/', views.admin_views_single_past_session),
    #######################################################################################################
    path('schooladmin/', views.school_admin_home),
    path('schooladmin/upcomingsessions/', views.school_admin_upcoming_sessions),
    path('schooladmin/upcomingsessions/<pk:int>/', views.school_admin_views_single_upcoming_session),
    path('schooladmin/upcomingsessions/<pk:int>/applications/',
         views.school_admin_views_single_upcoming_session_applications),
    path('schooladmin/upcomingsessions/<pk:int>/applications/<pk:int>/',
         views.school_admin_views_single_application_from_upcoming_session),
    path('schooladmin/pastsessions/', views.school_admin_past_sessions),
    path('schooladmin/pastsessions/<pk:int>/', views.school_admin_views_single_past_session),
    path('schooladmin/courses', views.school_admin_courses),
    path('schooladmin/courses/<pk:int>/', views.school_admin_views_single_course),
    path('schooladmin/addsession', views.school_admin_add_session),
    path('schooladmin/addcourse', views.school_admin_add_course),
]
