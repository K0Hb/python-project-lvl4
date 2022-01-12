from django.urls import path
from .views import HomePageView, UsersListView, RegisterUserView, \
    UserLoginView, UserLogout, UserDeleteView, UserUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('users/', UsersListView.as_view(), name='users_page'),
    path('users/create/', RegisterUserView.as_view(),
         name='sign_up_page'),
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('logout/', UserLogout.as_view(), name='logout_page'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(),
         name='delete_user'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(),
         name='update_user'),
]
