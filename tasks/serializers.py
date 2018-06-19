# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Task
from  auth_users.serializers import AuthUserModelSerializer 
from  auth_users.models import AuthUser
from  rates.serializers import RateModelSerializer
from  rates.models import Rate

# Serializers define the API representation.
class TaskModelSerializer(serializers.ModelSerializer):
    user = AuthUserModelSerializer(read_only=True)
    rate = RateModelSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'user', 'rate', 'active']
    
    def create(self, validated_data):
        task = Task(
            user_id=validated_data['user'],
            rate_id=validated_data['rate'],
            active=validated_data['active'],
        )
        task.save()
        return task