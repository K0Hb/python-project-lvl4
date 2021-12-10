from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AuthUserForm, RegisterUserForm, UserUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'main_page/home_page.html'

class UsersListView(ListView):
    model = User
    template_name = 'main_page/users_list.html'
    context_object_name = 'users_list'

class MyProjectLoginView(LoginView):
    template_name = 'main_page/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    success_message = 'Вы залогинены'
    def get_success_url(self):
        return self.success_url

class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    success_url = reverse_lazy('login_page')
    form_class = RegisterUserForm
    success_message = 'Пользователь успешно создан'
    template_name = 'main_page/users_create.html'

class UpdateUserView(UpdateView):
    pass

class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy('users')
    template_name = 'main_page/delete_user.html'
    pass