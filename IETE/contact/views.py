from django.shortcuts import render

# Create your views here.

def contact(request):
    content = {
        'name':'CONTACT',
    }
    return render(request, 'contact/contact.html', context=content)