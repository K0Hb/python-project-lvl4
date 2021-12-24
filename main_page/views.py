from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from .forms import RegisterUserForm, AuthUserForm, UserUpdateForm  # noqa: F401
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'home_page.html'


class UsersListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.all()


class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'mainpage/signup.html'
    success_url = reverse_lazy('login_page')
    form_class = RegisterUserForm
    success_message = 'Пользователь успешно создан'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'mainpage/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    success_message = 'Вы залогинены'

    def get_success_url(self):
        return self.success_url


class UserLogout(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Вы разлогинены')
        return response


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users_page')
    template_name = 'mainpage/delete_user.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'mainpage/user_update_form.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users')
