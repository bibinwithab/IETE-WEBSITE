from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from django.contrib import messages


def events(request):
    context = {
        'events':Event.objects.all(),
        'name' : 'EVENTS',
    }
    return render(request, 'events/event.html', context)
