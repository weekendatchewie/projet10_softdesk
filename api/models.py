from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"Utilisateur : {self.username}"


class Project(models.Model):
    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    IOS = 'IOS'
    ANDROID = 'ANDROID'

    TYPE_CHOICES = (
        (BACKEND, 'back-end'),
        (FRONTEND, 'front-end'),
        (IOS, 'ios'),
        (ANDROID, 'android'),
    )

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Contributor(models.Model):
    pass