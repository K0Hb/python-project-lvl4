from django.db import models
from status.models import Status
from tags.models import Tags
from main_page.models import MyUser as User
# from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField('Имя', max_length=75)
    description = models.TextField(
        'Description',
        max_length=200,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.ForeignKey(
        Status,
        blank=True,
        null=True,
        related_name='Статус',
        on_delete=models.PROTECT,
        verbose_name='Статусы'
    )
    creator = models.ForeignKey(
        User,
        related_name='Создаетль',
        on_delete=models.PROTECT,
        verbose_name='Создатели'
    )
    executor = models.ForeignKey(
        User,
        verbose_name='Исполнители',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='Испольнитель',
    )

    tags = models.ManyToManyField(
        Tags,
        blank=True,
        verbose_name='Метки',
        related_name='Метка',
    )

    @property
    def full_name(self):
        return '%s %s' % (self.executor.first_name, self.executor.last_name)

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name
