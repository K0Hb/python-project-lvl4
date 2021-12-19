from django.forms import ModelForm
from tasks.models import Task
import django_filters


class RegisterTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = "Имя"


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['creator', 'status', 'tags', 'executor']
