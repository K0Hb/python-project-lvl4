from django.forms import ModelForm
from tasks.models import Task
import django_filters


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['creator', 'status', 'tags', 'executor']


class RegisterTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'tags')
        labels = {'labels': 'Метки'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Имя"
        self.fields['description'].label = "Описание"
        self.fields['status'].label = "Статус"
        self.fields['executor'].label = "Испольнитель"
        self.fields['tags'].label = "Метки"
