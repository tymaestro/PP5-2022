from django.shortcuts import get_object_or_404
from products.models import Tour


def basket_contents(request):

    basket_items = []
    grand_total = 0
    tour_count = 0

    context = {
        'basket_items': basket_items,
        'grand_total': grand_total,
        'tour_count': tour_count,
    }

    return context
