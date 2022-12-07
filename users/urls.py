from django.urls import path
from .views import RegisterVolunteerView

urlpatterns = [
    path('register/volunteer', RegisterVolunteerView.as_view()),
    #path('login', LoginView.as_view()),
    #path('user', UserView.as_view()),
    #path('logout', LogoutView.as_view()),
]