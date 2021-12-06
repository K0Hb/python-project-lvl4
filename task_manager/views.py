from django.shortcuts import render, redirect, reverse
from task_manager.models import Users


def index(request):

    data = {
        'title': 'Мененджер Задач $'
    }
    return render(request, 'task_manager/base_page.html', context=data)


def users(request):
    data_class = {
        'users': Users.objects.all(),
    }
    return render(request, 'task_manager/users.html', context=data_class)


def login(request):
    return render(request, 'task_manager/login.html')


def create(request):
    return render(request, 'task_manager/create.html')

