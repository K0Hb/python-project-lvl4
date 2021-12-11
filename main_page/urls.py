from django.urls import path, include
from .views import HomePageView, UsersListView
from . import views
from .views import SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='index_url'),
    path('', HomePageView.as_view(), name='home'),
    path('users/', UsersListView.as_view(), name='users_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='sign_up_url'),
    path('accounts/signup/', views.SignUpView.as_view(), name='sign_up_url'),
]