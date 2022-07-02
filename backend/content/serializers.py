from rest_framework import serializers
from .models import *
from .likes import is_liked as liked


class ContentSerializerMixin:
    is_liked = serializers.SerializerMethodField()
    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return liked(obj, user)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer, ContentSerializerMixin):
    class Meta:
        model = Article
        fields = '__all__'

class

