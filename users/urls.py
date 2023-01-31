from django.urls import path
from .views import RegisterVolunteerView , RegisterStudentView, RegisterAdminView, RegisterSchoolAdminView, LoginView,UserView,LogoutView
from .volunteerViews import getMySessions,applyToSession,getMyPendingSessions
urlpatterns = [
    path('register/volunteer', RegisterVolunteerView.as_view()),
    path('register/student', RegisterStudentView.as_view()),
    path('register/admin', RegisterAdminView.as_view()),
    path('register/schooladmin', RegisterSchoolAdminView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('volunteer/mysessions', getMySessions),
    path('volunteer/applysession', applyToSession),
    path('volunteer/mypendingsessions', getMyPendingSessions),
]