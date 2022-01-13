from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()
