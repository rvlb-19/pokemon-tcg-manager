from django.apps import AppConfig

class CardsConfig(AppConfig):
    name = 'cards'

    def ready(self):
        import cards.signals