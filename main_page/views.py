from django.views.generic.list import ListView
from main_page.models import CustomUser as User
from django.views.generic.base import TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class HomePageView(TemplateView):
    template_name = 'home_page.html'


class UsersListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.all()
