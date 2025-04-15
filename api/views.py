from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from .models import Message
from .serializers import MessageSerializer, CreateUserSerializer


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(self.request)
        print(self.request.headers)
        print(self.request.user)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # only for dev purposes
        user = User.objects.all()[0]
        serializer.save(user=user)


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]