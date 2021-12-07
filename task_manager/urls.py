"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from task_manager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls),
    path('task-manager/', views.index, name='start_page'),
    path('task-manager/users', views.users, name='users_table'),
    path('task-manager/login', views.login, name='login'),
    path('task-manager/users/create', views.create, name='resgistration'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
