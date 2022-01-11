from django.shortcuts import redirect
from django.views.generic.list import ListView
from main_page.models import MyUser as User
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterUserForm  # noqa: F401
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext as _
from tasks.models import Task

USER_REG = _('Пользователь успешно зарегистрирован')
USER_LOG = _('Вы залогинены')
USER_OUTLOG = _('Вы разлогинены')
USER_DEL = _('Пользователь успешно удалён')
USER_NOT_DEL = _(
    'Невозможно удалить пользователя, потому что он используется')
USER_UPD = _('Пользователь успешно изменён')


class HomePageView(TemplateView):
    template_name = 'home_page.html'


class UsersListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users_list'


class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'mainpage/signup.html'
    success_url = reverse_lazy('login_page')
    form_class = RegisterUserForm
    success_message = USER_REG


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'mainpage/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    success_message = USER_LOG

    def get_success_url(self):
        return self.success_url


class UserLogout(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, USER_OUTLOG)
        return response


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users_page')
    template_name = 'mainpage/delete_user.html'
    success_message = USER_DEL

    def delete(self, request, *args, **kwargs):
        if Task.objects.filter(creator=self.request.user.pk) \
                or Task.objects.filter(executor=self.request.user.pk):
            messages.error(self.request, USER_NOT_DEL)
            return redirect(reverse_lazy('users_page'))

        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'mainpage/user_update_form.html'
    success_url = reverse_lazy('users_page')
    success_message = USER_UPD
    form_class = RegisterUserForm
