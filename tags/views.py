from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from tags.models import Tags
from tags.forms import RegisterTagForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TagsListView(LoginRequiredMixin, ListView):
    model = Tags
    template_name = 'tags/tags_list.html'
    context_object_name = 'tags_list'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class CreateTagView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tags
    template_name = 'tags/tag_create.html'
    form_class = RegisterTagForm
    success_url = reverse_lazy('tags')
    success_message = "Метка успешно создана"
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class UpdateTagView(LoginRequiredMixin, UpdateView):
    model = Tags
    template_name = 'tags/tag_update.html'
    form_class = RegisterTagForm
    success_url = reverse_lazy('tags')
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Метка успешно изменена')
        return response


class DeleteTagView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Tags
    success_url = reverse_lazy('tags')
    template_name = 'tags/tag_delete.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Метка успешно удалена')
        return response