
from typing import Any
from django import http
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/home.html'
    def home(self,request):
        return render(request, 'home/index.html', {'name':'Home'})