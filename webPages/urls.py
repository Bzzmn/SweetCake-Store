from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('contact/', views.contact, name='contact'),
    path('exito/', views.exito, name='exito'),
]

