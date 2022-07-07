from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from users.models import CustomUser


class Like(models.Model):
    user = models.ForeignKey(CustomUser, related_name='likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


# Добавление лайка к дженерику
def add_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    if is_created:
        obj.rating += 1
        obj.creator.rating += 1
        obj.save()
        user.save()


# Удаление лайка из дженерика
def remove_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    like = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    )

    if like.exists():
        like.delete()
        obj.rating -= 1
        user.rating -= 1
        obj.save()
        user.save()


# Проверяет, лайкнул ли `user` `obj`
def is_liked(obj, user) -> bool:
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return likes.exists()


# Mixin для контента(Постов, комментов)
class ContentAPIMixin(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericAPIView):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        like = self.request.query_params.get('like')
        unlike = self.request.query_params.get('unlike')
        if like is not None:
            add_like(instance, self.request.user)

        if unlike is not None:
            remove_like(instance, self.request.user)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
