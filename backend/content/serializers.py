from rest_framework import serializers
from .models import *
from .likes import is_liked as liked

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return liked(obj, user)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    creator_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return obj.creator.username
    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return liked(obj, user)

    class Meta:
        model = Comment
        fields = '__all__'


