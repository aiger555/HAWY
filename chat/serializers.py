from rest_framework import serializers

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import Chat, Contact, Message


User = get_user_model()


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')


class ContSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants')
        read_only = ('id')
        depth = 1

    def create(self, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.save()
        for username in participants:
            contact = get_user_contact(username)
            chat.participants.add(contact)
        chat.save()
        return chat