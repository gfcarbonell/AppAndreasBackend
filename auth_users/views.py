# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets

from .models import AuthUser
from django.contrib.auth.models import Group
from .serializers import AuthUserModelSerializer, GroupModelSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class AuthUserModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserModelSerializer
    queryset_detail  = queryset.prefetch_related('groups__permissions')
    permission_classes = (IsAuthenticated,)

    
class GroupModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    permission_classes = (IsAuthenticated,)
    
# View Pseudocode
from rest_framework.authtoken.models import Token

def token_request(request):
    if user_requested_token() and token_request_is_warranted():
        new_token = Token.objects.create(user=request.user)