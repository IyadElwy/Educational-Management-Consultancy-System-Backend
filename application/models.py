from django.db import models
from session.models import Session
from users.models import Volunteer

class Application(models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,
                              choices=[
                                  ('In Process', 'In Process'),
                                  ('Accepted', 'Accepted'),
                                  ('Rejected', 'Rejected'),
                              ], default='In Process')
    # Connectors
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.session.course.name} - {self.status}'
