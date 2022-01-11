from django.forms import ModelForm
from tasks.models import Task
import django_filters
from django.utils.translation import gettext as _


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['creator', 'status', 'labels', 'executor']


class RegisterTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'labels')
        labels = {'labels': _('Метка'),
                  'creator': _('Создатель'),
                  'status': _('Статус')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = _("Имя")
        self.fields['description'].label = _("Описание")
        self.fields['status'].label = _("Статус")
        self.fields['executor'].label = _("Исполнитель")
        self.fields['labels'].label = _("Метки")
