from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.utils.translation import gettext as _

class HomePageView(TemplateView):
    extra_context = {'title': _('Главная страница')}
    template_name = 'main_page/home_page.html'

class UsersListView(ListView):
    model = User
    extra_context = {'title': _('Список пользователей')}
    template_name = 'main_page/users_list.html'
    context_object_name = 'users_list'

class MyProjectLoginView(LoginView):
    extra_context = {'title': _('Аутентификация')}
    template_name = 'main_page/login.html'

class RegisterUserView(CreateView):
    extra_context = {'title': _('Регистрация')}
    template_name = 'main_page/users_create.html'