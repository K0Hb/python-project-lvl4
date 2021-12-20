import django_filters
from tasks.models import Task
from tags.models import Tags

from django.forms.widgets import CheckboxInput


class TaskFilter(django_filters.FilterSet):
    own_tasks = django_filters.BooleanFilter(
        method='filter_own_tasks',
        # field_name='creator',
        widget=CheckboxInput
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user).order_by('pk')
        return queryset

    tags = django_filters.ModelChoiceFilter(
        queryset=Tags.objects.all(),
    )

    class Meta:
        model = Task
        fields = ['executor', 'status', 'tags', 'creator']
