from rest_framework import serializers
from .models import *
from .models_subscription import *


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscribtion
        fields = '__all__'


class TagSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagSubscribtion
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'rating', 'avatar']
