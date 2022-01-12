import django as tables
from django.utils.translation import gettext as _
from status.models import Status


class StatusesTable(tables.Table):
    class Meta:
        model = Status
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'create_date', 'links')
        attrs = {
            'button_name': _('Create'),
            'class': 'table table-striped'
        }
