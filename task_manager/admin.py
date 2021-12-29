from django.contrib import admin
from status.models import Status
from labels.models import Labels
from tasks.models import Task


admin.site.register(Status)
admin.site.register(Labels)
admin.site.register(Task)
