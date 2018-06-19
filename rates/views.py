# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets

from .models import Rate
from .serializers import RateModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class RateModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rate.objects.all()
    serializer_class = RateModelSerializer
    permission_classes = (IsAuthenticated,)