from django.db import models
from django.contrib.auth.models import User



class Message(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')


