from django.db import models


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_priority = models.IntegerField()
    task_description = models.TextField()

    def __str__(self):
        return self.task_name
