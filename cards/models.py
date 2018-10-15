from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import perform_request

def build_set_choices():
    r = perform_request('sets')
    return list(map(lambda x: (x['code'], x['name']), r['sets']))

CHOICES = build_set_choices()

class Collection(models.Model):
    name = models.CharField(_('name'), max_length=20, choices=CHOICES, default=CHOICES[0], unique=True)

    class Meta:
        verbose_name = _('collection')
        verbose_name_plural = _('collections')
        ordering = ('id',)
    
    def __str__(self):
        return self.get_name_display()

class Card(models.Model):
    # Became a CharField for rare cases where the number is a letter
    number = models.CharField(_('number'), max_length=10, null=True)
    name = models.CharField(_('name'), max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    supertype = models.CharField(_('supertype'), max_length=255)
    subtype = models.CharField(_('subtype'), max_length=255, null=True)
    first_type = models.CharField(_('first type'), max_length=255, null=True)
    second_type = models.CharField(_('second type'), max_length=255, null=True)
    rarity = models.CharField(_('rarity'), max_length=255, null=True)
    sequence = models.PositiveIntegerField(_('sequence'), null=True)

    class Meta:
        verbose_name = _('card')
        verbose_name_plural = _('cards')
        ordering = ('collection', 'sequence')
    
    def __str__(self):
        return self.name
    
    @classmethod
    def create_from_dict(cls, obj):
        extra_fields = {}
        try:
            extra_fields['first_type'] = obj['types'][0]
            extra_fields['second_type'] = obj['types'][1]
        except (IndexError, KeyError):
            pass
        
        try:
            extra_fields['rarity'] = obj['rarity']
        except KeyError:
            pass
        
        number = obj['number']

        try:
            sequence = int(number)
        except ValueError:
            # Offsets the sequence to a large number using the letter ASCII code
            sequence = 500 + ord(number)
                
        card = {
            'number': number,
            'name': obj['name'],
            'collection': Collection.objects.get(name=obj['setCode']),
            'supertype': obj['supertype'],
            'subtype': obj['subtype'],
            'sequence': sequence,
            **extra_fields,
        }

        cls(**card).save()