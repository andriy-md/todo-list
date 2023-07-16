from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskSolver(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=65, unique=True)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    is_done = models.BooleanField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
