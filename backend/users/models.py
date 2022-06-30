from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    rating = models.IntegerField(default=0)
    status = models.CharField(max_length=255)
    avatar = models.ImageField(default='default_avatar.png', upload_to='avatars')

    def __str__(self):
        return self.username


