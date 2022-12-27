from django.contrib import admin
from .models import Application

admin.site.register(Application)
admin.site.site_header = "EMCS"
admin.site.site_title = "EMCS Admin Portal"
admin.site.index_title = "Welcome to the Educational Management Consultancy System"
