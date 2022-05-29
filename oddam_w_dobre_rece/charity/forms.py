from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': ('Imię')})
        self.fields['last_name'].widget.attrs.update({'placeholder': ('Nazwisko')})
        self.fields['email'].widget.attrs.update({'placeholder': ('Email')})
        self.fields['password1'].widget.attrs.update({'placeholder': ('Hasło')})
        self.fields['password2'].widget.attrs.update({'placeholder': ('Powtórz hasło')})