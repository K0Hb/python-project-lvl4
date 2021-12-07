from django.urls import path, include
from .views import HomePageView, UsersListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('users/', UsersListView.as_view(), name='users'),
]