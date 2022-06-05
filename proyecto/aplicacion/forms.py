from django import forms
from django.db.models import fields
from .models import Cliente
from django.contrib.auth.models import User

class ReclamoForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    reclamo = forms.CharField(widget=forms.Textarea)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido')

grupos =(
    ("grupo1", "Grupo Numero 1"),
    ("grupo2", "Grupo Numero 2"),
)
class UsuariosForm(forms.Form):
    grupos =(
    ("grupo1", "Grupo Numero 1"),
    ("grupo2", "Grupo Numero 2"),
    )
    nombre = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    grupo= forms.ChoiceField(choices = grupos)

class LoginForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class GeeksForm(forms.Form):
    group = forms.ChoiceField(choices = grupos)