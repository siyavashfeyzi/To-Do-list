from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    PRIORITY_LOW = 'L'
    PRIORITY_MEDIUM = 'M'
    PRIORITY_TOP = 'T'

    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Low'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_TOP, 'Top'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title
