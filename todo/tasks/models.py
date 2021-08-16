from django.db import models
from .choices import STATUS_CHOICE


class Task(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)

    def __str__(self):
        return f"{self.name} - {self.created_at}"
