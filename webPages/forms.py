from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.db import transaction


class ContactFormForm(forms.Form):
  customer_email = forms.EmailField(label='Correo', required=True, widget=forms.EmailInput(attrs={'placeholder': 'Tu correo electrónico', 'class': 'form-control'}))
  customer_name = forms.CharField(label='Nombre', required=True, max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class': 'form-control'}) )
  message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí', 'class': 'form-control'}))

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
    help_texts = {
            'username': 'Ingresa tu nombre de usuario.',
            'password1': 'Ingresa tu password.',
            'password2': 'Ingresa tu password nuevamante.',
        }
  def save(self, commit=True):
      user = super(CustomUserCreationForm, self).save(commit=False)
      if commit:
          with transaction.atomic(): 
              user.save()
              group, created = Group.objects.get_or_create(name="Usuarios Web")
              user.groups.add(group)
      return user

