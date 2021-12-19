import django_filters
from tasks.models import Task


# from django.forms.widgets import CheckboxInput


class TaskFilter(django_filters.FilterSet):
    # own_tasks = django_filters.BooleanFilter(
    #     field_name='creator',
    #     widget=CheckboxInput
    # )
    #
    # def filter_own_tasks(self, queryset, name, value):
    #     if value:
    #         return queryset.filter(creator=self.request.user).order_by('pk')
    #     return queryset

    class Meta:
        model = Task
        fields = ['executor', 'status', 'tags', 'creator']
