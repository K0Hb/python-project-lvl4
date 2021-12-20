from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls),
    path('statuses/', include('status.urls')),
    path('tasks/', include('tasks.urls')),
    path('lebels/', include("tags.urls")),
]
