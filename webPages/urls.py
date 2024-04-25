from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('contact/', views.contact, name='contact'),
    path('registro/', views.register, name='registro'),
    path('cupcakes/<slug:slug>/', views.productPage, {'product_type': 'cupcake'}, name='cupcake_detalle'),
    path('tortas/<slug:slug>/', views.productPage, {'product_type': 'torta'}, name='torta_detalle'),
    path('cupcakes/', views.cupcakesPage, name='cupcakes'),
    path('tortas/', views.tortasPage, name='tortas'),
]