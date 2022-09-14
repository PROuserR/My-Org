from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SubTask(models.Model):
    content = models.CharField(max_length=255)
    checked = models.BooleanField(default=False)

class Task(models.Model):
    owner = models.ForeignKey('auth.User', related_name='Task', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    subtask = models.ManyToManyField(to=SubTask)
    created = models.DateTimeField(auto_now_add=True)
    reminder = models.DateTimeField()

class Note(models.Model):
    owner = models.ForeignKey('auth.User', related_name='Note', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)