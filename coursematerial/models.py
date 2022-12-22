from django.db import models
from session.models import Session
from users.models import Volunteer,School_Admin
class SchoolMaterial(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    uploaded_by = models.ForeignKey(School_Admin, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} - {self.session.course.name}'


class VolunteerMaterial(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    description = models.TextField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.session.course.name}'
