""" system module """
from django.apps import AppConfig


class ShopConfig(AppConfig):
    """ shop config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
