from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User


def create_profile(instance, created, sender, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(sender=User, receiver=create_profile)
