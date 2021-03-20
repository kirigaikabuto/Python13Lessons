from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateField(default=timezone.now)
    deadline = models.DateField()
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
