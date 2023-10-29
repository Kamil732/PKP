from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from .models import Account

class AccountAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(
        label = 'Email adres',
        max_length = 60,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class': 'login-input',
                'id': 'email-input',
                'placeholder': 'Type your email here...',
            }
        )
    )

    password = forms.CharField(
        required = True,
        label = 'Hasło',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'login-input',
                'id': 'password-input',
                'placeholder': 'Type your password here...',
            }
        )
    )

    class Meta:
        model = Account
        fields = (
            'email',
            'password',
        )

    def clean(self, *args, **kwargs):
        if self.is_valid:
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label = 'Email adres',
        max_length = 60,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class': 'login-input',
                'id': 'email-input',
                'placeholder': 'Type your email here...',
            }
        )
    )

    password1 = forms.CharField(
        required = True,
        label = 'Hasło',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'login-input',
                'id': 'password-input',
                'placeholder': 'Type password here...',
            }
        )
    )

    password2 = forms.CharField(
        required = True,
        label = 'Powtórz hasło',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'login-input',
                'id': 'password-confirm-input',
                'placeholder': 'Type your password again...',
            }
        )
    )

    username = forms.CharField(
        required = True,
        max_length = 60,
        label = 'Nazwa użytkownika',
        widget = forms.TextInput(
            attrs = {
                'class': 'login-input',
                'id': 'username-input',
                'placeholder': 'Type username here...',
            }
        )
    )

    class Meta:
        model = Account
        fields = (
            'email',
            'username',
            'password1',
            'password2',
        )

class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label = 'Email adres',
        max_length = 60,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class': 'login-input',
                'id': 'email-input',
                'placeholder': 'Type your email here...',
            }
        )
    )

    username = forms.CharField(
        required = True,
        max_length = 60,
        label = 'Nazwa użytkownika',
        widget = forms.TextInput(
            attrs = {
                'class': 'login-input',
                'id': 'username-input',
                'placeholder': 'Type username here...',
            }
        )
    )

    class Meta:
        model = Account
        fields = (
            'email',
            'username',
        )

    def clean_email(self):
        if self.is_valid:
            email = self.cleaned_data.get('email')
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
        raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid:
            username = self.cleaned_data.get('username')
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
        raise forms.ValidationError('username "%s" is already in use.' % account.username)