from django.db import models
from session.models import Session


class Application(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,
                              choices=[
                                  ('In Process', 'In Process'),
                                  ('Accepted', 'Accepted'),
                                  ('Rejected', 'Rejected'),
                              ], default='In Process')

    def __str__(self):
        return f'{self.session.course.name} - {self.status}'
