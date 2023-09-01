from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def contact(request):
    content = {
        'name':'CONTACT',
    }
    if request == 'POST':
        name = request.POST['name']
        mail = request.POST['email']
        message = request.POST['message']
    
        return HttpResponse("<h1>Thank You</h1>")

    return render(request, 'contact/contact.html', context=content)