from django.db import models
from status.models import Status
from labels.models import Labels
from main_page.models import MyUser as User


class Task(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=75
    )
    description = models.TextField(
        'Description',
        max_length=200,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    status = models.ForeignKey(
        Status,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Создатель'
    )
    executor = models.ForeignKey(
        User,
        verbose_name='Исполнитель',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='Испольнитель',
    )

    labels = models.ManyToManyField(
        Labels,
        blank=True,
        verbose_name='Метка',
    )

    @property
    def full_name(self):
        return '%s %s' % (self.executor.first_name, self.executor.last_name)

    def __str__(self):
        return self.name
