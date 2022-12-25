from django.contrib import admin
from .models import User, Volunteer, Student, Admin, School_Admin

# Register your models here.
admin.site.register(User)
admin.site.register(Volunteer)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(School_Admin)
