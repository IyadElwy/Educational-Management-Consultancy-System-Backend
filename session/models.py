from django.db import models
from course.models import Course
from rating.models import MLScore, StudentRating, CoordinatorRating
from django.db.models import Avg


class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.course.school} - {self.course.name} {self.start_time.strftime("%d/%m/%Y")}'

    def get_avg_ratings(self):
        ml_scores = MLScore.objects.filter(session_id=self.pk)
        if len(ml_scores) == 0:
            return self.avg_student(), self.avg_coordinator(), 'No Rating Yet'
        else:
            return self.avg_student(), self.avg_coordinator(), ml_scores[0]

    def avg_coordinator(self):
        coordinator_scores = CoordinatorRating.objects.filter(session_id=self.pk)
        question_1_avg = coordinator_scores.aggregate(Avg('question_1'))['question_1__avg']
        question_2_avg = coordinator_scores.aggregate(Avg('question_2'))['question_2__avg']
        question_3_avg = coordinator_scores.aggregate(Avg('question_3'))['question_3__avg']
        question_4_avg = coordinator_scores.aggregate(Avg('question_4'))['question_4__avg']
        question_5_avg = coordinator_scores.aggregate(Avg('question_5'))['question_5__avg']
        question_6_avg = coordinator_scores.aggregate(Avg('question_6'))['question_6__avg']

        try:
            return (question_1_avg +
                    question_2_avg +
                    question_3_avg +
                    question_4_avg +
                    question_5_avg +
                    question_6_avg) / 6.0
        except Exception as e:
            return 'No Rating Yet'

    def avg_student(self):
        student_scores = StudentRating.objects.filter(session_id=self.pk)
        question_1_avg = student_scores.aggregate(Avg('question_1'))['question_1__avg']
        question_2_avg = student_scores.aggregate(Avg('question_2'))['question_2__avg']
        question_3_avg = student_scores.aggregate(Avg('question_3'))['question_3__avg']
        question_4_avg = student_scores.aggregate(Avg('question_4'))['question_4__avg']
        question_5_avg = student_scores.aggregate(Avg('question_5'))['question_5__avg']
        question_6_avg = student_scores.aggregate(Avg('question_6'))['question_6__avg']
        question_7_avg = student_scores.aggregate(Avg('question_7'))['question_7__avg']
        question_8_avg = student_scores.aggregate(Avg('question_8'))['question_8__avg']
        question_9_avg = student_scores.aggregate(Avg('question_9'))['question_9__avg']
        question_10_avg = student_scores.aggregate(Avg('question_10'))['question_10__avg']
        question_11_avg = student_scores.aggregate(Avg('question_11'))['question_11__avg']

        try:
            return (question_1_avg +
                    question_2_avg +
                    question_3_avg +
                    question_4_avg +
                    question_5_avg +
                    question_6_avg +
                    question_7_avg +
                    question_8_avg +
                    question_9_avg +
                    question_10_avg +
                    question_11_avg) / 6.0
        except Exception as e:
            return 'No Rating Yet'
