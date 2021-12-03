from django.shortcuts import render, redirect, reverse


def index(request):

    data = {
        # 'users': 'users',
        # 'login': 'login',
        # 'create': 'users/create',
        # 'task_manager': '',
        'title': 'Мененджер Задач $'
    }
    return render(request, 'task_manager/base_page.html', context=data)


def users(request):
    class experiment:
        def __init__(self):
            self.id = 1
            self.firstname = 'Vasja'
            self.lastname = 'Pupkin'
            self.created_at = '22.08.1991'
            self.link_change = '#'
            self.link_delete = '#'
    lol = experiment()
    lol1 = experiment()
    data_class = {
        'users': [lol , lol1]
    }
    return render(request, 'task_manager/users.html', context=data_class)


def login(request):
    return render(request, 'task_manager/login.html')


def create(request):
    return render(request, 'task_manager/create.html')

