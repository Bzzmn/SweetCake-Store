from django import forms

class ContactFormForm(forms.Form):
  customer_email = forms.EmailField(label='Correo', required=True, widget=forms.EmailInput(attrs={'placeholder': 'Tu correo electrónico', 'class': 'form-control'}))
  customer_name = forms.CharField(label='Nombre', required=True, max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Tu nombre', 'class': 'form-control'}) )
  message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí', 'class': 'form-control'}))