from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Conversation, Message

@receiver(post_save, sender=Conversation)
def generate_summary(sender, instance, **kwargs):
    # Generate a summary of the conversation
    messages = Message.objects.filter(version__conversation=instance).order_by('created_at')
    summary = "\n".join([message.content for message in messages[:5]])  # Simple summary of first 5 messages
    instance.summary = summary
    instance.save()

# In chat/apps.py, add the following to ready method
from django.apps import AppConfig

class ChatConfig(AppConfig):
    name = 'chat'

    def ready(self):
        import chat.signals