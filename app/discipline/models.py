from django.db import models


class Discipline(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)

    class Meta:
        verbose_name = "Учебная дисциплина"
        verbose_name_plural = "Учебные дисциплины"
        ordering = ["-name"]

    def __str__(self):
        return self.name
