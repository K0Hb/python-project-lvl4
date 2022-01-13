from django import forms  # noqa: F401
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.utils.translation import gettext as _


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('Password')})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Password Confirmation')})
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('User name')})
        self.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Name')})
        self.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Surname')})
