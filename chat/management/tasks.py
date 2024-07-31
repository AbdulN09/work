from backend.celery import shared_task
from django.core.management import call_command

@shared_task
def cleanup_old_conversations():
    call_command('cleanup_conversations')

