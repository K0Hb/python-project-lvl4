from django.urls import path
from tasks.views import TasksListView, CreateTaskView

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('', TasksListView.as_view(), name='update_task'),
    path('', TasksListView.as_view(), name='delete_task'),
]
