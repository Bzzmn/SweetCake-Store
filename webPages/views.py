# pylint: disable=no-member

from django.shortcuts import render, redirect, get_object_or_404, Http404
from .models import Torta, Cupcake
from .forms import ContactFormForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    public_tortas = Torta.objects.filter(is_private=False)
    featured_tortas = Torta.objects.filter(is_featured=True)

    public_cupcakes = Cupcake.objects.filter(is_private=False)
    featured_cupcakes = Cupcake.objects.filter(is_featured=True)

    num_tortas = Torta.objects.count()
    num_cupcakes = Cupcake.objects.count()

    tortas_exclusive = Torta.objects.filter(is_private=True).count()
    cupcakes_exclusive = Cupcake.objects.filter(is_private=True).count()

    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tortas": num_tortas,
        "num_cupcakes": num_cupcakes,
        "public_tortas": public_tortas,
        "public_cupcakes": public_cupcakes,
        "featured_tortas": featured_tortas,
        "featured_cupcakes": featured_cupcakes,
        "tortas_exclusive": tortas_exclusive,
        "cupcakes_exclusive": cupcakes_exclusive,
        "num_visits": num_visits,
    }

    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")


@login_required
def welcome(request):
    private_tortas = Torta.objects.filter(is_private=True)
    private_cupcakes = Cupcake.objects.filter(is_private=True)

    context = {
        "private_tortas": private_tortas,
        "private_cupcakes": private_cupcakes,
    }
    return render(request, "pages/welcome.html", context)


def contact(request):
    if request.method == "POST":
        print(request.POST)
        form = ContactFormForm(request.POST)
        if form.is_valid():
            messages.success(request, "Tu mensaje fue enviado")
            return redirect(to="index")

    else:
        form = ContactFormForm()
        return render(request, "pages/contact.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="welcome")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def productPage(request, product_type, slug):
    model_dict = {"cupcake": Cupcake, "torta": Torta}
    model = model_dict.get(product_type)
    if not model:
        raise Http404("Producto no encontrado")

    product = get_object_or_404(model, slug=slug)
    product.visit_count += 1
    product.save()

    category_url = reverse(f"{product_type}s")
    product_url = reverse(
        "cupcake_detalle" if product_type == "cupcake" else "torta_detalle", args=[slug]
    )

    breadcrumb = [
        {"title": "Inicio", "url": reverse("index")},
        {"title": product_type.capitalize() + "s", "url": category_url},
        {"title": product.name, "url": product_url},
    ]

    context = {"producto": product, "breadcrumb": breadcrumb}

    return render(request, "pages/product-page.html", context)


def cupcakesPage(request):
    public_products = Cupcake.objects.filter(is_private=False)
    featured_products = Cupcake.objects.filter(is_featured=True)
    num_products = Cupcake.objects.count()
    exclusive_products = Cupcake.objects.filter(is_private=True).count()
    num_visits = request.session.get("num_visits_cupcakes", 0)
    request.session["num_visits_cupcakes"] = num_visits + 1

    context = {
        "public_products": public_products,
        "featured_products": featured_products,
        "num_products": num_products,
        "exclusive_products": exclusive_products,
        "num_visits": num_visits,
        "product_type": "cupcake",
    }
    return render(request, "pages/category-page.html", context)


def tortasPage(request):
    public_products = Torta.objects.filter(is_private=False)
    featured_products = Torta.objects.filter(is_featured=True)
    num_products = Torta.objects.count()
    exclusive_products = Torta.objects.filter(is_private=True).count()
    num_visits = request.session.get("num_visits_tortas", 0)
    request.session["num_visits_tortas"] = num_visits + 1

    context = {
        "public_products": public_products,
        "featured_products": featured_products,
        "num_products": num_products,
        "exclusive_products": exclusive_products,
        "num_visits": num_visits,
        "product_type": "torta",
    }
    return render(request, "pages/category-page.html", context)


def loginForm(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
    else:
        form = AuthenticationForm()
        form.fields["username"].widget.attrs.update(
            {"class": "form-control", "style": "background-color: #FFF;"}
        )
        form.fields["password"].widget.attrs.update(
            {"class": "form-control", "style": "background-color: #FFF;"}
        )

    return render(request, "login.html", {"form": form})
