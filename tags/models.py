from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        verbose_name = 'Метки'
        verbose_name_plural = 'Метка'

    def __str__(self):
        return self.name
