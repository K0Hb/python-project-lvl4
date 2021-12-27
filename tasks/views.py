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
from django.contrib.auth.models import User
from django.contrib import messages

TASK_CREATE = "Задача успешно создана"
TASK_DEL = 'Задача успешно удалена'
TASK_NOT_DEL = 'Невозможно удалить пользователя, потому что он используется'
TASK_UPD = 'Задача успешно изменена'


class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login_page')
    model = Task
    form_class = RegisterTaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks')
    success_message = TASK_CREATE
    extra_context = {
        'title': 'Создать задачу',
        'button_name': 'Создать'
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
    extra_context = {'title': 'Изменение задачи'}


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
                      context={'task': model, 'tags_list': model.tags})


class TasksListView(LoginRequiredMixin, FilterView):
    login_url = '/login/'
    model = Task
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter
