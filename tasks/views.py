from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django_filters.views import FilterView

from tasks.filters import TaskFilter
from tasks.models import Task
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.forms import RegisterTaskForm
from users.models import MyUser as User
from django.contrib import messages
from tasks.tables import TasksTable
from django_tables2 import SingleTableView
from django.utils.translation import gettext as _

TASK_CREATE = _("The task was successfully created")
TASK_DEL = _('The task was successfully deleted')
TASK_NOT_DEL = _(
    'It is not possible to delete a user because it is being used')
TASK_UPD = _('The task has been successfully changed')


class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Task
    form_class = RegisterTaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks')
    success_message = TASK_CREATE
    extra_context = {
        'title': _('Create task'),
        'button_name': _('Create')
    }

    def form_valid(self, form):
        form.instance.creator = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login_page')
    model = Task
    form_class = RegisterTaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks')
    success_message = TASK_UPD
    extra_context = {'title': _('Changing the task')}


class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/task_delete.html'
    login_url = reverse_lazy('login_page')
    success_message = TASK_DEL

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            self.success_message
        )
        return super(DeleteTaskView, self).delete(self.request,
                                                  *args, **kwargs)


class TaskView(View):
    def get(self, request, pk):
        model = Task.objects.get(id=pk)
        return render(request, 'tasks/task_view.html',
                      context={'task': model, 'labels_list': model.labels})


class TasksListView(LoginRequiredMixin, FilterView, SingleTableView):
    login_url = '/login/'
    model = Task
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter
    table_class = TasksTable
