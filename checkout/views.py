from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LSknvBDlVjl8tOm3Y1HV6BUP4885DIbqRz1OczVV6PrfmcAkgjswgl56dJPU8yYaRi9aYaiKVWf29kvH3ZzVfdC00Zed3ADwI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
