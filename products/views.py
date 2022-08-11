from django.shortcuts import render, get_object_or_404
from .models import Tour


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
