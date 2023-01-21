from account.models import CustomUser
from django.db import models


class Curator(CustomUser):
    class Meta:
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"
