from curator.models import Curator
from discipline.models import Discipline
from django.db import models


class Direction(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    curator = models.OneToOneField(
        verbose_name="Куратор",
        to=Curator,
        on_delete=models.PROTECT,
        related_name="direction",
    )
    disciplines = models.ManyToManyField(
        verbose_name="Дисциплины", to=Discipline, related_name="directions"
    )

    class Meta:
        verbose_name = "Направление подготовки"
        verbose_name_plural = "Направления подготовки"
        ordering = ["-name"]

    def __str__(self):
        return self.name
