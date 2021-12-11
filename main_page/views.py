from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm



class HomePageView(TemplateView):
    template_name = 'home_page.html'

class UsersListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users_list'
    def get_queryset(self):
        return User.objects.all()

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"