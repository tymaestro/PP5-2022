""" system module """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<tour_id>/', views.add_to_basket, name='add_to_basket'),
    path('update/<tour_id>/', views.update_basket, name='update_basket'),
    path('delete/<tour_id>/',
         views.delete_from_basket,
         name='delete_from_basket'),
]
