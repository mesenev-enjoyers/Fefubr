from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=255, blank=True, default="")
    avatar = models.ImageField(default='default_avatar.png', upload_to='avatars')
    telegram = models.CharField(max_length=50, blank=True, default="") # chat_id
    # REQUIRED_FIELDS = ['rating', 'status']

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-rating']


