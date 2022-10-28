from django.db import models


class Wallet(models.Model):
    points = models.FloatField()

    def __str__(self):
        return f'{self.points}'
