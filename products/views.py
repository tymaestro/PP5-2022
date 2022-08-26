from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tour


from .forms import TourForm


def all_tours(request):

    tours = Tour.objects.all()

    context = {
        'tours': tours,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):

    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_detail.html', context)


@login_required
def add_tour(request):
    """ Add a tour to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this action is restricted to site owners.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            messages.error(request,
                           ('Failed to add tour. '
                            'Please ensure the form is valid.'))
    else:
        form = TourForm()

    template = 'products/add_tour.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_tour(request, tour_id):
    """ Edit a tour on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this action is restricted to site owners.')
        return redirect(reverse('home'))

    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated tour!')
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            messages.error(request,
                           ('Failed to update tour. '
                            'Please ensure the form is valid.'))
    else:
        form = TourForm(instance=tour)
        messages.info(request, f'You are editing {tour.tour_title}')

    template = 'products/edit_tour.html'
    context = {
        'form': form,
        'tour': tour,
    }

    return render(request, template, context)


@login_required
def delete_tour(request, tour_id):
    """ Delete a tour from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this action is restricted to site owners.')
        return redirect(reverse('home'))

    tour = get_object_or_404(Tour, pk=tour_id)
    tour.delete()
    messages.success(request, 'Tours deleted!')
    return redirect(reverse('tours'))
