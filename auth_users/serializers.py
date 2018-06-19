# -*- encoding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import AuthUser
import sys
from django.core import exceptions
import django.contrib.auth.password_validation as validators

# Serializers define the API representation.
class AuthUserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'password', 'email', 'is_active', 'is_superuser' ]
        read_only_fields = ['is_staff', 'is_superuser', 'is_active', 'data_joined']
        write_only_fields = ['password']
    
    def create(self, validated_data):
        user = AuthUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permission
		fields = '__all__'

class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')