from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'main_page/home_page.html'

class UsersListView(ListView):
    model = User
    template_name = 'main_page/users_list.html'
    context_object_name = 'users_list'
