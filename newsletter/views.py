""" system module """
from django.shortcuts import render
from django.contrib import messages

from .models import NewsletterSubscriber
from .forms import NewsletterSignupForm


def newsletter_signup(request):
    """ newsletter signup view """
    form = NewsletterSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterSubscriber.objects.filter(email=instance.email).exists():
            messages.error(request,
                           ('Your email address '
                            'already exists in our database'))
        else:
            instance.save()
            messages.success(request,
                             ('Thanks for subscribing! '
                              'Your email address has been added '
                              'to our mailing list'))

    context = {
        'form': form,
    }

    template = 'newsletter/signup.html'
    return render(request, template, context)


def newsletter_unsubscribe(request):
    """ newsletter unsubscribe view """
    form = NewsletterSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterSubscriber.objects.filter(email=instance.email).exists():
            NewsletterSubscriber.objects.filter(email=instance.email).delete()
            messages.success(request,
                             ('Your email '
                              'has been deleted from our database'))
        else:
            messages.error(request,
                           ('The email address you provided '
                            'was not found in our database'))

    context = {
        'form': form,
    }

    template = 'newsletter/unsubscribe.html'
    return render(request, template, context)
