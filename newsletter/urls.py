from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_signup, name='newsletter_signup'),
    path('', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),
]
