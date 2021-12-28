from django import forms  # noqa: F401
from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm
# from django.contrib.auth.models import User
from main_page.models import MyUser as User


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Подтверждение пароля'})
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Имя пользователя'})
        self.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Имя'})
        self.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Фамилия'})

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name']


class AuthUserForm(AuthenticationForm):
    # username = UsernameField(
    #     label='Имя пользователя',
    #     widget=forms.TextInput(attrs={ 'placeholder': 'Имя пользователя'})
    # )
    # password = UsernameField(
    #     label = 'Пароль',
    #     widget=forms.PasswordInput(attrs={ 'placeholder': 'Пароль'})
    # )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Пароль'})

    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'password')

# class UserUpdateForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'password')
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={'placeholder': 'Имя пользователя'}),
#             'first_name': forms.TextInput(
#                 attrs={'placeholder': 'Имя'}),
#             'last_name': forms.TextInput(
#                 attrs={'placeholder': 'Фамилия'}),
#             'password': forms.PasswordInput(
#                 attrs={'placeholder': 'Пароль'})
#         }
