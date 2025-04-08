from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MessageSerializer
from .models import Message
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # only for dev purposes
        user = User.objects.all()[0]
        serializer.save(user=user)
