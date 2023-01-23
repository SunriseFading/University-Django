from account.models import CustomUser
from django.db import models
from group.models import Group


class Student(CustomUser):
    group = models.ForeignKey(verbose_name="Группа", to=Group, on_delete=models.CASCADE, related_name="students")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["-group"]
