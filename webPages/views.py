from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Torta, ContactForm
from .forms import ContactFormForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index (request):
    public_tortas = Torta.objects.filter(is_private=False)
    featured_tortas = Torta.objects.filter(is_featured=True)

    num_tortas=Torta.objects.count()
    tortas_exclusivas = Torta.objects.filter(is_private=True).count()
    
    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_tortas':num_tortas,
        'num_visits':num_visits,
        'public_tortas':public_tortas,
        'featured_tortas':featured_tortas,
        'tortas_exclusivas':tortas_exclusivas,
    }

    return render(request, 'pages/index.html', context)

def about (request):
    return render(request, 'pages/about.html')

@login_required
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
            messages.success(request, 'Tu mensaje fue enviado')
            return redirect(to='index')

    else:
        form = ContactFormForm()
        return render(request, 'pages/contact.html', {'form':form})

def register (request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
                login(request, user)
                messages.success(request, 'Te has registrado correctamente')
                return redirect(to='welcome') 
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

def productPage (request, slug):
    torta = get_object_or_404(Torta, slug=slug)
    torta.visit_count += 1
    torta.save()
    return render(request, 'pages/product-page.html', {'torta':torta})























































































































