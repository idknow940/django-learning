from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    article = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"
