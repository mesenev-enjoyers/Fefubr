from django.contrib.auth.models import AbstractUser
from django.db import models
from content.models import *


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    rating = models.IntegerField(default=0)
    status = models.CharField(max_length=255)
    avatar = models.ImageField(default='default_avatar.png', upload_to='avatars')

    def __str__(self):
        return self.username


class UserSubscribtion(models.Model):
    user = models.ForeignKey(CustomUser, related_name='subscribed_user_on_user', on_delete=models.CASCADE)
    subscribe = models.ForeignKey(CustomUser, related_name='subscribe_target', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'subscribe')


class TagSubscribtion(models.Model):
    user = models.ForeignKey(CustomUser, related_name='subscribed_user_on_tag', on_delete=models.CASCADE)
    tag_subscribe = models.ForeignKey(Tag, related_name='subscribe_tag', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'tag_subscribe')
