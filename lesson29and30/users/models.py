from django.db import models
from django.utils import timezone
from django.conf import settings


class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    action = models.CharField(max_length=255)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} -> {self.action} -> {self.created_time}"