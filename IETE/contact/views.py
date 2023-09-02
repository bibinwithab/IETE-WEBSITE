from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Contact


# Create your views here.

def contact(request):
    content = {
        'name':'CONTACT',
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, message=message)

    

        return HttpResponse('<h1>thank-you. Your response is recorded</h1>')

    return render(request, 'contact/contact.html', context=content)