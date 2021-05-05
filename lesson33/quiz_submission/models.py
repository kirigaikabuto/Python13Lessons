from django.db import models
from django.contrib.auth.models import User
from quiz.models import *


class QuestionSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)


# Create your models here.
class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = models.ManyToManyField(QuestionSubmission)
