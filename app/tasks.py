from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger

# from channels.layers import get_channel_layer

from django.utils import timezone
from django.contrib.auth.models import User

from .models import Message

@shared_task
def save_user_messages(user_id, messages):
    user = User.objects.get(pk=user_id)
    
    for message_text in messages:
        message = Message(user=user, message=message_text, timestamp=timezone.now())
        message.save()
    
    print('Message Saved')