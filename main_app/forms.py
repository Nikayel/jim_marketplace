from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'w-full py-4 px-6 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-50'}))
    password1 = forms.CharField(widget = forms.TextInput(attrs={'class': 'w-full py-4 px-6 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-50'}))

class SignUpForm(UserCreationForm):
    class Meta:
         model = User
         fields = ('username', 'email', 'password1','password2')

    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'w-full py-4 px-6 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-50'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'placeholder': '...@gmail.com', 'class': 'w-full py-4 px-6 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-50'}))
    password1 = forms.CharField(widget = forms.TextInput(attrs={'class': 'w-full py-4 px-6 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-50'}))
    password2 = forms.CharField(widget = forms.TextInput(attrs={ 'class': 'w -full py-4 px-6 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-50'}))