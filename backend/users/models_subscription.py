from django.db import models

from content.models import Tag
from .models import CustomUser


class UserSubscribtion(models.Model):
    user = models.ForeignKey(CustomUser, related_name='subscribed_user_on_user', on_delete=models.CASCADE)
    subscribe = models.ForeignKey(CustomUser, related_name='subscribe_target', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' subscribed to ' + str(self.subscribe)

    class Meta:
        unique_together = ('user', 'subscribe')


class TagSubscribtion(models.Model):
    user = models.ForeignKey(CustomUser, related_name='subscribed_user_on_tag', on_delete=models.CASCADE)
    tag_subscribe = models.ForeignKey(Tag, related_name='subscribe_tag', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' subscribed to tag ' + str(self.tag_subscribe)

    class Meta:
        unique_together = ('user', 'tag_subscribe')
