from django.shortcuts import render
from django.contrib import messages

from .models import NewsletterSubscriber
from .forms import NewsletterSignupForm


def newsletter_signup(request):
    form = NewsletterSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterSubscriber.objects.filter(email=instance.email).exists():
            messages.error(request,
                           (f'The email {form.email} '
                            f'already exists in our database'))
        else:
            instance.save()

    context = {
        'form': form,
    }

    template = 'newsletter/subscription.html'
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = NewsletterSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterSubscriber.objects.filter(email=instance.email).exists():
            NewsletterSubscriber.objects.filter(email=instance.email).delete()
            messages.success(request,
                             (f'The email {form.email} '
                              f'has been deleted from our database'))
        else:
            messages.error(request,
                           (f'The email {form.email} '
                            f'was not found in our database'))

    context = {
        'form': form,
    }

    template = 'newsletter/unsubscribe.html'
    return render(request, template, context)
