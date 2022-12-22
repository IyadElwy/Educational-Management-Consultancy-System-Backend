from django.db import models
class Rating(models.Model):
    StudentRating = models.OneToOneField(StudentRating)
    CoordinatorRating = models.OneToOneField(CoordinatorRating)
    MLScore = models.OneToOneField(MLScore)
class CoordinatorRating(models.Model):
    pass


class StudentRating(models.Model):
    pass


class MLScore(models.Model):
    pass
