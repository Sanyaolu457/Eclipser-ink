from .models import Participant
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = Participant
        fields = ["username", "email", "phone_number", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "",
                "placeholder": ""
            }),
            "email": forms.EmailInput(attrs={
                "class": "",
                "placeholder": ""
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "",
                "placeholder": "Phone number"
            }),
        }

class UserLogin(AuthenticationForm):
    username = forms.CharField(
        label = '',
        widget= forms.TextInput(attrs={
            'class': '',
            'placeholder': 'Username or Email'
        })
    )

    password = forms.CharField(
        label= '',
        widget= forms.PasswordInput(attrs={
            'class': '',
            'placeholder': '**********'
        })
    )