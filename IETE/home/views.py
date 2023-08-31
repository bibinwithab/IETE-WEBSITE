# from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

# class HomePageView(TemplateView):
    # template_name = 'home/home.html'

def home(request):
    content = {
        'name':'HOME',
    }
    return render(request, 'home/home.html', context=content)
