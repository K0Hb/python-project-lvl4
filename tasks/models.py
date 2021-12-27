from django.db import models
from status.models import Status
from tags.models import Tags
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(
        'Description',
        max_length=200,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        blank=True,
        null=True,
        related_name='status',
        on_delete=models.PROTECT,
        verbose_name='Status'
    )
    creator = models.ForeignKey(
        User,
        related_name='creator',
        on_delete=models.PROTECT,
        verbose_name='Creator'
    )
    executor = models.ForeignKey(
        User,
        verbose_name='Executor',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='executor'
    )

    tags = models.ManyToManyField(
        Tags,
        blank=True,
        verbose_name='Tags',
        related_name='Tags',
    )

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name
