from django.db import models
from course.models import Course


class SchoolMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} - {self.course.name}'

# class VolunteerMaterial(models.Model):
#     session = models.ForeignKey(Session, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     description = models.TextField()
#     is_public = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.name} - {self.session.course.name}'
