""" system module """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order

from .models import UserProfile
from .forms import UserProfileForm


@login_required()
def profile(request):
    """ function to render profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    user = request.user
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, template, context)


@login_required
def update_profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/update_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ function to get order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
