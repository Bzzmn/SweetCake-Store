from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Torta, ContactForm
from .forms import ContactFormForm

# Create your views here.

def index (request):
    public_tortas = Torta.objects.filter(is_private=False)
    return render(request, 'pages/index.html', {'public_tortas':public_tortas})

def about (request):
    return render(request, 'pages/about.html')

def welcome (request):
    private_tortas = Torta.objects.filter(is_private=True)
    return render(request, 'pages/welcome.html', {'private_tortas':private_tortas})

def contact (request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # return render(request, 'pages/modal-exito.html')
            return redirect('exito')

    else:
        form = ContactFormForm()
        return render(request, 'pages/contact.html', {'form':form})

def exito (request):
    return render(request, 'pages/exito.html')