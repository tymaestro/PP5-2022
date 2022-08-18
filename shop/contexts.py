from django.shortcuts import get_object_or_404
from products.models import Tour


def basket_contents(request):

    basket_items = []
    total = 0
    tour_count = 0
    basket = request.session.get('basket', {})

    for tour_id, quantity in basket.items():
        tour = get_object_or_404(Tour, pk=tour_id)
        total += quantity * tour.tour_price
        tour_count += quantity
        basket_items.append({
            'tour_id': tour_id,
            'quantity': quantity,
            'tour': tour,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'tour_count': tour_count,
    }

    return context
