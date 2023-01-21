from account.models import CustomUser
from django.db import models


class Curator(CustomUser):
    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"
