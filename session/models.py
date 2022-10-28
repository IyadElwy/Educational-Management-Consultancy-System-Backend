from django.db import models
from course.models import Course


class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.course.school} - {self.course.name} {self.start_time.strftime("%d/%m/%Y")}'
