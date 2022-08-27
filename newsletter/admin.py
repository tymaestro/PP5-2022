from django.contrib import admin

from .models import NewsletterSubscriber


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscription_date',)


admin.site.register(NewsletterSubscriber, NewsletterAdmin)
