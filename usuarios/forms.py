# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Rol

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), label="Rol", widget=forms.Select(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label="Teléfono", widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email', 'rol', 'telefono', 'direccion']

    def save(self, commit=True):
        # Crear usuario en User y asociarlo con Usuario
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        usuario = Usuario(user=user, rol=self.cleaned_data['rol'],
                          telefono=self.cleaned_data['telefono'],
                          direccion=self.cleaned_data['direccion'])
        if commit:
            usuario.save()
        return usuario

class CustomUserEditForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), label="Rol", widget=forms.Select(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label="Teléfono", widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['password', 'email', 'rol', 'telefono', 'direccion']
