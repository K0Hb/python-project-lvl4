import django_tables2 as tables
from django.utils.translation import gettext as _
from tasks.models import Task


class TasksTable(tables.Table):
    TEMPLATE = '''
        <a href="{% url 'update_task' record.pk %}"
         class="tbl_icon edit">{{ edit }}</a>
        <br>
        <a href="{% url 'delete_task' record.pk %}"
         class="tbl_icon delete">{{ delete }}</a>
    '''
    links = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name='',
        extra_context={'edit': _('Change'), 'delete': _('Delete')}
    )

    name = tables.TemplateColumn(
        '<a href="{% url \'view_task\' record.pk %}">{{ record.name }}</a>'
    )

    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'status', 'creator', 'executor',
                  'created_at')
        attrs = {
            'class': 'table table-striped'
        }
