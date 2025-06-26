from django import forms

class SubscribeForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    contraseña = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contraseña'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo'}))