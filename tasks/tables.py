import django_tables2 as tables
from tasks.models import Task


class TasksTable(tables.Table):
    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'status', 'creator', 'executor',
                  'created_at', 'tags')
        attrs = {
            'class': 'table table-striped'
        }
