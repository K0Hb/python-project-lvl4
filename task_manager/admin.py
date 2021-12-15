from django.contrib import admin
from main_page.models import CustomUser
from status.models import Status
from tags.models import Tags
from tasks.models import Task

admin.site.register(CustomUser)
admin.site.register(Status)
admin.site.register(Tags)
admin.site.register(Task)
