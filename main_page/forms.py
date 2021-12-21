from django import forms  # noqa: F401
from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Имя пользователя'}),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Фамилия'}),
            'password1': forms.PasswordInput(
                attrs={'placeholder': 'Password'}),
        }


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Имя пользователя'}),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Пароль'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Имя пользователя'}),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Фамилия'}),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Пароль'})
        }
