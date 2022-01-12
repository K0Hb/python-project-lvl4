from django import forms  # noqa: F401
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': _('Пароль')})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Подтверждение пароля')})
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Имя пользователя')})
        self.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Имя')})
        self.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': _('Фамилия')})

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name']
