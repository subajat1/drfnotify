from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import permissions, renderers, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import models, serializers

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
