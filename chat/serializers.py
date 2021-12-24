from rest_framework import serializers

from accounts.models import User

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'message', 'timestamp', )