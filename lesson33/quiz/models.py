from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + "_" + self.owner.username
