from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    deadline = models.DateTimeField()

