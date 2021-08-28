from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    field = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="profile_images", default="static/user/images/default.png")

    def __str__(self):
        return f"{self.user.username}"
