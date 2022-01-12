from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('statuses/', include('status.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include("labels.urls")),
]
