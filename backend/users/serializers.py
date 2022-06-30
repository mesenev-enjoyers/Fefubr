from rest_framework import serializers
from .models import *


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscribtion
        fields = '__all__'


class TagSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagSubscribtion
        fields = '__all__'
