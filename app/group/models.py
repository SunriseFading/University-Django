from direction.models import Direction
from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    direction = models.ForeignKey(
        verbose_name="Направление", to=Direction, on_delete=models.CASCADE, related_name="groups"
    )

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
        ordering = ["-name"]

    def __str__(self):
        return self.title
