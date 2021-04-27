from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + "_" + self.owner.username


class QuestionAnswer(models.Model):
    name = models.CharField(max_length=255)


class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answers = models.ManyToManyField(QuestionAnswer)
    rightAnswer = models.OneToOneField(QuestionAnswer, on_delete=models.CASCADE, related_name="question_answers")
