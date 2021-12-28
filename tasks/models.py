from django.db import models
from status.models import Status
from tags.models import Tags
from main_page.models import MyUser as User
# from django.contrib.auth.models import User


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
        related_name='executor',
        # to_field = 'first_name'
    )

    tags = models.ManyToManyField(
        Tags,
        blank=True,
        verbose_name='Tags',
        related_name='Tags',
    )

    @property
    def full_name(self):
        return '%s %s' % (self.executor.first_name, self.executor.last_name)

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name
