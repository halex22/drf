from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
