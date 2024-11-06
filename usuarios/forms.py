from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Rol

class UsuarioForm(UserCreationForm):
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=True, label="Rol")
    telefono = forms.CharField(max_length=20, required=True, label="Teléfono")
    direccion = forms.CharField(max_length=255, required=True, label="Dirección")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Usuario.objects.create(
                user=user,
                rol=self.cleaned_data['rol'],
                telefono=self.cleaned_data['telefono'],
                direccion=self.cleaned_data['direccion']
            )
        return user
