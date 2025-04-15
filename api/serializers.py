from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User
from .models import Message


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ['text']


class CreateUserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            password= validated_data.get('password'),
            email= validated_data['email']
        )
        return user