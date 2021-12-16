from django.urls import path
from tags.views import TagsListView, CreateTagView, \
    UpdateTagView, DeleteTagView

urlpatterns = [
    path('', TagsListView.as_view(), name='tags'),
    path('create/', CreateTagView.as_view(), name='create_tag'),
    path('<int:pk>/update/', UpdateTagView.as_view(), name='update_tag'),
    path('<int:pk>/delete/', DeleteTagView.as_view(), name='delete_tag'),
]
