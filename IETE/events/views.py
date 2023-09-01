from django.http import HttpResponse
from django.shortcuts import render
from .models import Events

def events(request):
    context = {
        'events':Events.objects.all()
    }
    return render(request, 'events/event.html', context)