""" system module """
from django.db import models


class NewsletterSubscriber(models.Model):
    """ newsletter subscription model """
    email = models.EmailField()
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
