from django.db import models
from tinymce.models import HTMLField
from .choices import STATUS_CHOICE
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)

    def __str__(self):
        return f"{self.name} - {self.created_at}"
