# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Rate
import sys
from django.core import exceptions
import django.contrib.auth.password_validation as validators

# Serializers define the API representation.
class RateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['id', 'lot', 'location', 'rate', 'description', 'observation']