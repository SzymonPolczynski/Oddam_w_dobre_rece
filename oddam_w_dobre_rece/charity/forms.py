from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Donation


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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=254, label="Login",
                               widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['quantity', 'categories', 'institution', 'address', 'phone_number', 'city',
                  'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment']
