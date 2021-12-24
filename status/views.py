from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from status.models import Status
from status.forms import RegisterStatusesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status/statuses_list.html'
    context_object_name = 'statuses_list'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'status/statuses_create.html'
    form_class = RegisterStatusesForm
    success_url = reverse_lazy('statuses')
    success_message = "Статус успешно создан"
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class UpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    form_class = RegisterStatusesForm
    success_url = reverse_lazy('statuses')
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Статус успешно изменен')
        return response


class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    template_name = 'status/statuses_delete.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

    # def delete(self, request, *args, **kwargs):
    #     try:
    #         result = super().delete(request, *args, **kwargs)
    #         messages.success(request, self.success_message)
    #         return result
    #     except Exception:
    #         messages.error(request, self.protected_message)
    #     return redirect(self.success_url)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Статус успешно удален')
        return response
