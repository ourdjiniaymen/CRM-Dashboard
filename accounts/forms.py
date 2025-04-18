from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Order

class OrderForm(ModelForm):
    class Meta:
        model       = Order
        fields      = '__all__'
        
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model       = User
        fields      = ['username', 'email', 'password1', 'password2']

    username        = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Username'}))
    email           = forms.EmailField(widget = forms.EmailInput(attrs = {'placeholder':'Email'}))
    password1        = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Password'}))
    password2        = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'repeat password'}))