from django.db import models
from django.utils.translation import gettext_lazy as _


class Labels(models.Model):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=20,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True
    )

    class Meta(object):
        verbose_name = _('Метки')
        verbose_name_plural = _('Метка')

    def __str__(self):
        return self.name
