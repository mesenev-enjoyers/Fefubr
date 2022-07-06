from rest_framework import serializers
from .models import *
from .models_subscription import *


class UserSubscriptionSerializer(serializers.ModelSerializer):
    subscribe_name = serializers.SerializerMethodField()

    def get_subscribe_name(self, obj):
        return obj.subscribe.username

    class Meta:
        model = UserSubscribtion
        fields = '__all__'


class TagSubscriptionSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    def get_tag_name(self, obj):
        return obj.tag_subscribe.name

    class Meta:
        model = TagSubscribtion
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'rating', 'avatar']
