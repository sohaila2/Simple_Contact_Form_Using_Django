from django.shortcuts import render,redirect
from django.http import HttpResponse
from form.models import Contact

# Create your views here.


def index(request):
    
    if request.method=="POST":
        contact = Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return redirect('thank_you')  

    return render(request,'form/index.html')

def thankYou(request):
    return render(request, 'form/thank_you.html')