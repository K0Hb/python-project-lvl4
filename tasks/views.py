from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from tasks.models import Task
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.forms import RegisterTaskForm

class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks_list'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = RegisterTaskForm
    success_url = reverse_lazy('tasks')
    success_message = "Задача успешно создана"
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)