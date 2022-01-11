import django_filters
from tasks.models import Task
from labels.models import Labels

from django.forms.widgets import CheckboxInput
from django.utils.translation import gettext as _


class TaskFilter(django_filters.FilterSet):
    own_tasks = django_filters.BooleanFilter(
        label='Только свои задачи',
        method='filter_own_tasks',
        field_name='creator',
        widget=CheckboxInput
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Labels.objects.all(),
        label=_('Метка')
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user).order_by('pk')
        return queryset

    class Meta:
        model = Task
        fields = ['executor', 'status', 'labels', 'creator']
        filter_overrides = {
            django_filters.BooleanFilter: {
                'extra': lambda f: {'widget': CheckboxInput},
                'filter_class': django_filters.BooleanFilter,
            },
        }
