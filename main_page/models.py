# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.get_full_name()
    # full_name = models.CharField(
    # max_length=150,
    # blank=True,
    # null=True,
    # verbose_name=_('Полное имя'))

    # def save(self, *args, **kw):
    #     self.full_name =f'{self.first_name} {self.last_name}'
    #     super(MyUser, self).save(*args, **kw)

    # def __str__(self):
    #     return self.full_name
