from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    user_1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'user_1',
        default = None,
    )
    user_2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'user_2',
        default = None,
    )
    messages = models.ManyToManyField (
        'Message', related_name='messages'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    