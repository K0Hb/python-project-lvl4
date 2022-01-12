from django.db import models
from django.utils.translation import gettext_lazy as _


class Labels(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=20,
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name=_('Date of creation'),
        auto_now_add=True
    )

    class Meta(object):
        verbose_name = _('Labels')
        verbose_name_plural = _('Label')

    def __str__(self):
        return self.name
