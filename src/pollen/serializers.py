from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('url', 'id', 'username')
    
class ContentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.Content
        fields = ('id', 'name', 'sender')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.Message
        fields = ('content', 'head_payload', 'body_payload', 'url_payload')