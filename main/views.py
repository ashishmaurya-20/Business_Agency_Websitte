from django.shortcuts import render
from .models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'index.html') 

def contact(request):
    if request.method == 'POST':
        name = request.POST['fname'] + " " + request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        reason = request.POST['reason']
        country = request.POST['country']
        message = request.POST['message']

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            reason=reason,
            country=country,
            message=message
        )
        messages.success(request, "Your message has been sent and saved!")
    return render(request, 'index.html')    
# Create your views here.
