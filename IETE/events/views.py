from django.http import HttpResponse
from django.shortcuts import render
from .models import Event, Registration
from .forms import RegisterForm


def events(request):
    context = {
        'events':Event.objects.all(),
        'name' : 'EVENTS',
    }
    return render(request, 'events/event.html', context)


def register(request):

    



    content = {
        'name':'REGISTER',
    }  

    return render(request, 'events/register.html', context=content)