""" system module """
from django import forms
from .models import Tour


class TourForm(forms.ModelForm):
    """ tour management form """

    class Meta:
        """ fields for tour management form """
        model = Tour
        exclude = ('schedule', )
    tour_image = forms.ImageField(label='Tour Image',
                                  required=True,)
