# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets

from .models import Task
from .serializers import TaskModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class TaskModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    permission_classes = (IsAuthenticated,)