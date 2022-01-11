from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from status.models import Status
from status.forms import RegisterStatusesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.utils.translation import gettext as _

STAT_CREATE = _("Статус успешно создан")
STAT_EDIT = _("Статус успешно изменён")
STAT_DEL = _("Статус успешно удалён")
STAT_NOT_DEL = _("Невозможно удалить статус, потому что он используется")


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status/statuses_list.html'
    context_object_name = 'statuses_list'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class CreateStatusView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    login_url = 'login'
    model = Status
    form_class = RegisterStatusesForm
    template_name = 'status/statuses_create.html'
    success_url = reverse_lazy('statuses')
    success_message = STAT_CREATE
    extra_context = {
        'title': 'Создать статус',
        'button_name': 'Создать'
    }

    def handle_no_permission(self):
        messages.error(
            self.request,
            "о"
        )


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    form_class = RegisterStatusesForm
    success_url = reverse_lazy('statuses')
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'
    success_message = STAT_EDIT
    extra_context = {
        'title': 'Изменение статуса',
        'button_name': 'Изменить'
    }


class DeleteStatusView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    template_name = 'status/statuses_delete.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'
    success_message = STAT_DEL

    def delete(self, request, *args, **kwargs):
        self.get_object()
        try:
            super(DeleteStatusView, self).delete(self.request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                self.request,
                STAT_NOT_DEL,
            )
        else:
            messages.success(
                self.request,
                self.success_message,
            )
        return redirect(self.success_url)
