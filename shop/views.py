""" system module """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Tour


def view_basket(request):
    """ function to view basket """
    return render(request, 'basket/basket.html')


def add_to_basket(request, tour_id):
    """ function to add to basket """
    tour = get_object_or_404(Tour, pk=tour_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if tour_id in list(basket.keys()):
        basket[tour_id] += quantity
        messages.success(request,
                         (f'Updated {tour.tour_title} '
                          f'quantity to {basket[tour_id]}'))
    else:
        basket[tour_id] = quantity
        messages.success(request, f'Added {tour.tour_title} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def delete_from_basket(request, tour_id):
    """ function to delete items from basket """
    basket = request.session.get('basket', {})

    basket.pop(tour_id)
    request.session['basket'] = basket

    return redirect(reverse('view_basket'))
