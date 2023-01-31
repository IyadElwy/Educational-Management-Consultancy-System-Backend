from django.db import models
from course.models import Course
from users.models import Volunteer

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    taught_by = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING, null=True, blank=True)
    #class_location = models.charfield(max_length=100)
    def __str__(self):
        return f'{self.course.school} - {self.course.name} {self.start_time.strftime("%d/%m/%Y")}'
