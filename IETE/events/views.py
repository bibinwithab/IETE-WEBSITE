from django.shortcuts import render
from .models import Event
from .forms import InputForm


def events(request):
    context = {
        'events':Event.objects.all(),
        'name' : 'EVENTS',
    }
    return render(request, 'events/event.html', context)


def register(request):
	context ={
        'name':'REGISTER'
    }
	context['form']= InputForm()
	return render(request, "events/register.html", context)
