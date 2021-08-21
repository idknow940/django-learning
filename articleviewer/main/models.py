from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=20)
    article = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"


class Comment(models.Model):
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_id = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment
