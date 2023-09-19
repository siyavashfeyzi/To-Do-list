from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
