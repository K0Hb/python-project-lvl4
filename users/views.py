from django.shortcuts import redirect
from django.views.generic.list import ListView
from users.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterUserForm  # noqa: F401
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.custom_mixin import AuthenticationVerification
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _
from tasks.models import Task

USER_REG = _('The user has been successfully registered')
USER_LOG = _('You are logged in')
USER_OUTLOG = _('You are logged out')
USER_DEL = _('The user has been successfully deleted')
USER_NOT_DEL = _(
    'It is not possible to delete a user because it is being used')
USER_UPD = _('User successfully changed')
USER_NOT_LOG = _('You are not authenticated')
USER_NOT_CREATOR = _('Only the user can delete himself')


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
    extra_context = {
        'title': _('Registration'),
        'button_name': _('Register')
    }


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


class UserDeleteView(AuthenticationVerification, SuccessMessageMixin,
                     LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users_page')
    template_name = 'mainpage/delete_user.html'
    success_message = USER_DEL
    message_not_authenticated = USER_NOT_CREATOR
    memessage_not_login = USER_NOT_LOG
    redirect_url_not_authenticated = 'users_page'

    def delete(self, request, *args, **kwargs):
        if Task.objects.filter(creator=self.request.user.pk) \
                or Task.objects.filter(executor=self.request.user.pk):
            messages.error(self.request, USER_NOT_DEL)
            return redirect(reverse_lazy('users_page'))

        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get(self, request, pk):
        object = self.get_object()
        if object.pk != self.request.user.pk:
            messages.error(
                self.request, self.message_not_authenticated,
            )
            return redirect(self.redirect_url_not_authenticated)
        return super().get(request, pk)


class UserUpdateView(AuthenticationVerification, SuccessMessageMixin,
                     LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'mainpage/user_update_form.html'
    success_url = reverse_lazy('users_page')
    success_message = USER_UPD
    form_class = RegisterUserForm
    message_not_authenticated = USER_NOT_CREATOR
    memessage_not_login = USER_NOT_LOG
    redirect_url_not_authenticated = 'users_page'

    def get(self, request, pk):
        object = self.get_object()
        if object.pk != self.request.user.pk:
            messages.error(
                self.request, self.message_not_authenticated,
            )
            return redirect(self.redirect_url_not_authenticated)
        return super().get(request, pk)
