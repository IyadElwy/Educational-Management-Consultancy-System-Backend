from django.db import models
from school.models import School


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    grade_level = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.school.name}'
