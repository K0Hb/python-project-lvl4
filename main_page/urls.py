from django.urls import path, include
from .views import HomePageView, UsersListView, MyProjectLoginView, RegisterUserView


urlpatterns = [
    # path('', index, name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('users/', UsersListView.as_view(), name='users'),
    path('login/', MyProjectLoginView.as_view(), name='login_page'),
    path('users/create/', RegisterUserView.as_view(), name='register_page'),
]