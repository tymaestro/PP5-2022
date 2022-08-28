""" system module """
from django import forms

from .models import NewsletterSubscriber


class NewsletterSignupForm(forms.ModelForm):
    """ newsletter signup form """
    class Meta:
        """ model and fields for newsletter signup """
        model = NewsletterSubscriber
        fields = ['email']
