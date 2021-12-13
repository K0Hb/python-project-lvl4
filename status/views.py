from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from status.models import Status
from status.forms import RegisterStatusesForm
from django.contrib.auth.mixins import LoginRequiredMixin


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


class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    template_name = 'status/statuses_delete.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'
