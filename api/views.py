from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(self.request.headers)
        print(self.request.user)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # only for dev purposes
        user = User.objects.all()[0]
        serializer.save(user=user)
