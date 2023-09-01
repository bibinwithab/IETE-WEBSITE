
from django.shortcuts import render
from .models import Event

def events(request):
    context = {
        'events':Event.objects.all(),
        'name' : 'EVENTS',
    }
    return render(request, 'events/event.html', context)