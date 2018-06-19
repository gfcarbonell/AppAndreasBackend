# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Task
from  auth_users.serializers import AuthUserModelSerializer 
from  auth_users.models import AuthUser
from  rates.serializers import RateModelSerializer
from  rates.models import Rate
from django.core.mail import EmailMessage



# Serializers define the API representation.
class TaskModelSerializer(serializers.ModelSerializer):
    user = AuthUserModelSerializer(read_only=True)
    rate = RateModelSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'user', 'rate', 'hour','active']

        
    def create(self, validated_data):
        print(validated_data)
        task = Task(
            user_id=1,
            rate_id=1,
            hour=validated_data['hour'],
            active=validated_data['active'],
        )
        return task