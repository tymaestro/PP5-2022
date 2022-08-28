""" system module """
from django.shortcuts import render


def index(request):
    """ returns home page view """
    return render(request, 'home/index.html')
