from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Tour


def view_basket(request):
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    tour = get_object_or_404(Tour, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                         (f'Updated {tour.tour_title} '
                          f'quantity to {basket[item_id]}'))
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {tour.tour_title} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    basket[item_id] = quantity
    request.session['basket'] = basket

    return redirect(redirect_url)


def delete_from_basket(request, item_id):
    basket = request.session.get('basket', {})

    basket.pop(item_id)
    request.session['basket'] = basket

    return redirect(reverse('view_basket'))
