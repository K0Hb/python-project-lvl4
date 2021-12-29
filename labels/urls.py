from django.urls import path
from labels.views import TagsListView, CreateTagView, \
    UpdateTagView, DeleteTagView

urlpatterns = [
    path('', TagsListView.as_view(), name='labels'),
    path('create/', CreateTagView.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateTagView.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteTagView.as_view(), name='delete_label'),
]
