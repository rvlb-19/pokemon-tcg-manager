from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Card, Collection
from .utils import perform_request

@receiver(post_save, sender=Collection)
def create_collection_cards(sender, instance, created, **kwargs):
    if created:
        r = perform_request('cards', { 'setCode': instance.name, 'pageSize': 400 })
        list(map(Card.create_from_dict, r['cards']))