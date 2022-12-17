from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ui.urls')),
    path('databaseadmin/', admin.site.urls),
    path('api/v1/school/', include('school.urls')),
    path('api/v1/course/', include('course.urls')),
    path('api/v1/session/', include('session.urls')),
    path('api/v1/application/', include('application.urls')),
    path('api/v1/wallet/', include('wallet.urls')),
    path('api/v1/material/', include('coursematerial.urls')),
    path('api/v1/users/', include('users.urls')),
]
