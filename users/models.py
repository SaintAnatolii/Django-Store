from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    SEX = [
        ('none', 'none'),
        ('fimale', 'fimale'),
        ('male', 'male'),
    ]
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    sex = models.CharField(max_length=9, choices=SEX, default="none")
    birthday = models.DateTimeField(blank=True, null=True)
