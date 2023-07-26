from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        to="Tag",
        related_name="tasks"
    )


class Tag(models.Model):
    name = models.CharField(max_length=255)
