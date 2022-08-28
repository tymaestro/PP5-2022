""" System module """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ checkout config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """ checkout signal """
        import checkout.signals
