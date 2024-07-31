from django.core.management.base import BaseCommand
from django.utils import timezone
from chat.models import Conversation

class Command(BaseCommand):
    help = 'Clean up old conversations'

    def handle(self, *args, **kwargs):
        threshold_date = timezone.now() - timezone.timedelta(days=30)
        old_conversations = Conversation.objects.filter(modified_at__lt=threshold_date)
        count = old_conversations.count()
        old_conversations.delete()
        self.stdout.write(f"Deleted {count} old conversations")

        