from django.urls import path, include
from . import views
from .views import productPage


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('contact/', views.contact, name='contact'),
    path('registro/', views.register, name='registro'),
    path('product/<slug:slug>/', productPage, name='producto'),
]