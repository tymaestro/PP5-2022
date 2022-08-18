from django.shortcuts import get_object_or_404
from products.models import Tour


def basket_contents(request):

    basket_items = []
    total = 0
    tour_count = 0
    basket = request.session.get('basket', {})

    for tour_id, tour_data in basket.items():
        if isinstance(tour_data, int):
            tour = get_object_or_404(Tour, pk=tour_id)
            total += tour_data * tour.tour_price
            tour_count += tour_data
            basket_items.append({
                'tour_id': tour_id,
                'quantity': tour_data,
                'tour': tour,
            })
        else:
            tour = get_object_or_404(Tour, pk=tour_id)
            for quantity in tour_data.items():
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
