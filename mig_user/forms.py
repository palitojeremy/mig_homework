from django import forms
from django.forms import ModelForm
from .models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
