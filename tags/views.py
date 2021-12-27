from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from tags.models import Tags
from tags.forms import RegisterTagForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import ProtectedError

TAG_CREATE = "Метка успешно создана"
TAG_EDIT = "Метка успешно изменена"
TAG_DEL = "Метка успешно удалена"
TAG_NOT_DEL = "Невозможно удалить метку, потому что она используется"


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
    success_message = TAG_CREATE
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'


class UpdateTagView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tags
    template_name = 'tags/tag_update.html'
    form_class = RegisterTagForm
    success_url = reverse_lazy('tags')
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'
    success_message = TAG_EDIT


class DeleteTagView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tags
    success_url = reverse_lazy('tags')
    template_name = 'tags/tag_delete.html'
    login_url = reverse_lazy('login_page')
    redirect_field_name = 'redirect_to'
    success_message = TAG_DEL

    def delete(self, request, *args, **kwargs):
        self.get_object()
        try:
            super(DeleteTagView, self).delete(self.request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                self.request,
                TAG_NOT_DEL,
            )
        else:
            messages.success(
                self.request,
                self.success_message,
            )
        return redirect(self.success_url)
