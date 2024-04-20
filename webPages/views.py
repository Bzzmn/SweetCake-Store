from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from .models import Torta, ContactForm, Cupcake
from .forms import ContactFormForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index (request):
    public_tortas = Torta.objects.filter(is_private=False)
    featured_tortas = Torta.objects.filter(is_featured=True)

    public_cupcakes = Cupcake.objects.filter(is_private=False)
    featured_cupcakes = Cupcake.objects.filter(is_featured=True)

    num_tortas=Torta.objects.count()
    num_cupcakes=Cupcake.objects.count()

    tortas_exclusive = Torta.objects.filter(is_private=True).count()
    cupcakes_exclusive = Cupcake.objects.filter(is_private=True).count()
    
    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_tortas':num_tortas,
        'num_cupcakes':num_cupcakes,
        'public_tortas':public_tortas,
        'public_cupcakes':public_cupcakes,
        'featured_tortas':featured_tortas,
        'featured_cupcakes':featured_cupcakes,
        'tortas_exclusive':tortas_exclusive,
        'cupcakes_exclusive':cupcakes_exclusive,
        'num_visits':num_visits,
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

def productPage(request, product_type, slug):
    model_dict = {
        'cupcake': Cupcake,
        'torta': Torta
    }
    model = model_dict.get(product_type)
    if not model:
        raise Http404("Producto no encontrado")
    
    product = get_object_or_404(model, slug=slug)
    product.visit_count += 1
    product.save()
    
    return render(request, 'pages/product-page.html', {'producto': product})


def cupcakesPage(request):
    public_products = Cupcake.objects.filter(is_private=False)
    featured_products = Cupcake.objects.filter(is_featured=True)
    num_products = Cupcake.objects.count()
    exclusive_products = Cupcake.objects.filter(is_private=True).count()
    num_visits = request.session.get('num_visits_cupcakes', 0)
    request.session['num_visits_cupcakes'] = num_visits + 1
    
    context = {
        'public_products': public_products,
        'featured_products': featured_products,
        'num_products': num_products,
        'exclusive_products': exclusive_products,
        'num_visits': num_visits,
        'product_type': 'cupcake'
    }
    return render(request, 'pages/category-page.html', context)

def tortasPage(request):
    public_products = Torta.objects.filter(is_private=False)
    featured_products = Torta.objects.filter(is_featured=True)
    num_products = Torta.objects.count()
    exclusive_products = Torta.objects.filter(is_private=True).count()
    num_visits = request.session.get('num_visits_tortas', 0)
    request.session['num_visits_tortas'] = num_visits + 1
    
    context = {
        'public_products': public_products,
        'featured_products': featured_products,
        'num_products': num_products,
        'exclusive_products': exclusive_products,
        'num_visits': num_visits,
        'product_type': 'torta'
    }
    return render(request, 'pages/category-page.html', context)













































































































































































































































