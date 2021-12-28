from django.forms import ModelForm
from tasks.models import Task
import django_filters


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['creator', 'status', 'tags', 'executor']
        labels = {'labels': 'Метки',
                  'creator': 'Создатель',
                  'status': 'Статус'}


class RegisterTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'tags')
        labels = {'labels': 'Метки',
                  'creator': 'Создатель',
                  'status': 'Статус'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
        self.fields['description'].label = "Описание"
        self.fields['status'].label = "Статус"
        self.fields['executor'].label = "Исполнитель"
        self.fields['tags'].label = "Метки"
