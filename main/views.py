from django.shortcuts import render, redirect

from .models import Contact


def home(request):
    return render(request, 'index.html')


def thank_you(request):
    return render(request, 'thankyou.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST["email"]
        message = request.POST["message"]

        contact_object = Contact.objects.create(
            name=name,
            email=email,
            subject=message
        )
        contact_object.save()

    return redirect('thank_you')

