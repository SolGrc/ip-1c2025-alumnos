from django import forms

class SubscribeForm(forms.Form):
    username = forms.CharField()
    name = forms.CharField()
    surname = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()