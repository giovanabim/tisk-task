from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm): # para o cadastro
    senha = forms.CharField(widget=forms.PasswordInput) # para ocultar os caracteres da senha
    class Meta:
        model = Usuario # o model que o formulario vai usar

        fields = ['nome', 'email', 'senha'] # os campos presentes no formulario

class LoginForm(forms.Form): # para o login
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )