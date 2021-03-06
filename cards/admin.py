from django.contrib import admin
from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .models import Card, Collection

class StyledModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin.css',)
        }
        js = ('js/admin.js',)

class CardAdmin(StyledModelAdmin):
    # change_view
    fields = ['card_image', 'name', 'number', 'collection_icon', 'supertype', 'subtype', 'rarity', 'typing']

    def get_fields(self, request, obj=None):
        fields = self.fields.copy()
        if not obj.first_type:
            fields.remove('typing')
        if not obj.rarity:
            fields.remove('rarity')
        if not obj.subtype:
            fields.remove('subtype')
        return fields
    
    def get_readonly_fields(self, request, obj=None):
        return self.get_fields(request, obj)
    
    def card_image(self, instance):
        set_code = instance.collection.name
        number = instance.number
        url = 'https://images.pokemontcg.io/{}/{}_hires.png'.format(set_code, number)
        img = '<img src="{}" class="card-img">'.format(url)
        return mark_safe(img)
    
    def collection_icon(self, instance):
        collection_code = instance.collection.name
        url = 'https://images.pokemontcg.io/{}/symbol.png'.format(collection_code)
        img = '<img src="{}" class="set-icon">'.format(url)
        return mark_safe(img)

    def typing(self, instance):
        types = [instance.first_type, instance.second_type]
        # This check occurs to deal with API data that has duplicate typings
        if types[0] == types[1]:
            types.pop()
        template = '<div class="energy-type {}" style="background-image: url({})"></div>'
        elements = [template.format(t.lower(), static('img/energy-types.png')) for t in types if t]
        return mark_safe('<div class="types-list">{}</div>'.format(''.join(elements)))
    
    # changelist_view
    list_display = ('number', 'card_image', 'name', 'collection_icon', 'typing',)
    list_display_links = ('name',)
    
    # Permissions    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Card, CardAdmin)

class CollectionAdmin(StyledModelAdmin):
    # change_view
    fields = ('collection_logo', 'name',)
    readonly_fields = ('collection_logo',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name',)
        return self.readonly_fields

    def collection_logo(self, instance):
        if isinstance(instance.name, tuple):
            # Used when a new collection is being added and the value come as a tuple
            collection_code = instance.name[0]
        else:
            # When the collection is being view and the value come as a str
            collection_code = instance.name
        url = 'https://images.pokemontcg.io/{}/logo.png'.format(collection_code)
        img = '<img src="{}" class="set-logo">'.format(url)
        return mark_safe(img)
    
    # changelist_view
    list_display = ('name', 'collection_icon', 'card_qnt', 'view_cards')
    def collection_icon(self, instance):
        collection_code = instance.name
        url = 'https://images.pokemontcg.io/{}/symbol.png'.format(collection_code)
        img = '<img src="{}" class="set-icon">'.format(url)
        return mark_safe(img)
    
    def card_qnt(self, instance):
        qnt = Card.objects.filter(collection=instance.pk).count()
        return _('{} cards'.format(qnt))
    
    def view_cards(self, instance):
        url = reverse('admin:cards_card_changelist')
        anchor = '<a href="{}?collection={}">{}</a>'.format(url, instance.pk, _('View cards'))
        return mark_safe(anchor)
    
    collection_icon.short_description = ''
    card_qnt.short_description = ''
    view_cards.short_description = ''

    # Permissions
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Collection, CollectionAdmin)
