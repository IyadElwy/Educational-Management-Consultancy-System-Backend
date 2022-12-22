from django.db import models

class CoordinatorRating(models.Model):
    pass


class StudentRating(models.Model):
    pass


class MLScore(models.Model):
    pass

class Rating(models.Model):
    StudentRating = models.OneToOneField(StudentRating , on_delete=models.CASCADE)
    CoordinatorRating = models.OneToOneField(CoordinatorRating , on_delete=models.CASCADE)
    MLScore = models.OneToOneField(MLScore , on_delete=models.CASCADE)