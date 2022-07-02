from rest_framework import serializers
from .models import *
from .likes import is_liked as liked


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return liked(obj, user)

