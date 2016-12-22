from django.shortcuts import render
from place.models import place


def index(request):
    return render(
        request,
        'index.html',
        {
            'places':Place.objects.all(),
        }
    )
