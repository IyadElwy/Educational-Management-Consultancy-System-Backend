from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CoordinatorRating(models.Model):
    session = models.ForeignKey(to='session.Session', on_delete=models.CASCADE)
    question_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]
                                     , verbose_name='The instructor’s attire was appropriate for the class')
    question_2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor looked put together')
    question_3 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor maintained a positive attitude')
    question_4 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor talked professionally refrained from harsh language')
    question_5 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor arrived on time')
    question_6 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor was easily contacted picked up phone etc')


class StudentRating(models.Model):
    session = models.ForeignKey(to='session.Session', on_delete=models.CASCADE)
    question_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='I feel like the instructor made the content feel easy to grasp('
                                                  'content felt appropriate to the level')
    question_2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='I feel the instructor understood my questions and motivated me to '
                                                  'ask intrusive questions')
    question_3 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='I feel that the language used in the class was appropriate for me '
                                                  'to understand(I felt that the language wasn’t too complicated)')
    question_4 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='I feel the instructors volume was audible and not unclear in any '
                                                  'way ')
    question_5 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='I feel the instructor showed full command of the subject ')
    question_6 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor answered all questions in a satisfactory manner')
    question_7 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor came in with a clear plan of how to lesson would go')
    question_8 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The Instructor handled any technical difficulties in a '
                                                  'professional manner')
    question_9 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                     verbose_name='The instructor was able to make sure the content was the right '
                                                  'level of challenging when they found that we weren’t responding')
    question_10 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                      verbose_name='I feel the instructor was able to maintain control over the '
                                                   'classroom ie other students were engaged as well')
    question_11 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                      verbose_name='I felt other peers did not affect the instructor’s performance')


class MLScore(models.Model):
    session = models.ForeignKey(to='session.Session', on_delete=models.CASCADE)
    percentage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Rating(models.Model):
    StudentRating = models.ForeignKey(StudentRating, on_delete=models.CASCADE, blank=True, null=True)
    CoordinatorRating = models.OneToOneField(CoordinatorRating, on_delete=models.CASCADE, blank=True, null=True)
    MLScore = models.OneToOneField(MLScore, on_delete=models.CASCADE, blank=True, null=True)
