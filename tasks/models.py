from django.db import models
from status.models import Status
from labels.models import Labels
from users.models import MyUser as User
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=75,
        unique=True
    )
    description = models.TextField(
        verbose_name=_('Discriptions'),
        max_length=200,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True
    )
    status = models.ForeignKey(
        Status,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name=_('Status')
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_('Creator')
    )
    executor = models.ForeignKey(
        User,
        verbose_name=_('Executor'),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name=_('Executor'),
    )

    labels = models.ManyToManyField(
        Labels,
        through='Task_Label',
        through_fields=('task_id', 'label_id'),
        blank=True,
        verbose_name=_('Labels'),
    )

    @property
    def full_name(self):
        return f'{self.executor.first_name} {self.executor.last_name}'

    def __str__(self):
        return self.name


class Task_Label(models.Model):
    task_id = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        verbose_name=_('Task_id')
    )
    label_id = models.ForeignKey(
        Labels,
        on_delete=models.PROTECT,
        verbose_name=_('Label_id')
    )
