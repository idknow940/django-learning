from django.db import models


class Task(models.Model):
    STATUS_CHOICES = (
        (0, "New"),
        (1, "Doing"),
        (2, "Done"),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.name} - {self.created_at} - {self.status}"
