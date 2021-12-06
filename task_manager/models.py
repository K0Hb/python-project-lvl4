from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    created_at = models.DateTimeField()
    link_change = models.CharField(max_length = 30)
    link_delete = models.CharField(max_length = 30)

    def __str__(self):
        return self.last_name