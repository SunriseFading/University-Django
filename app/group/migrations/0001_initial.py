# Generated by Django 4.1.5 on 2023-01-20 19:11

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("direction", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, verbose_name="Название")),
                (
                    "number_students",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(20),
                        ],
                        verbose_name="Количество студентов",
                    ),
                ),
                (
                    "direction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to="direction.direction",
                        verbose_name="Направление",
                    ),
                ),
            ],
            options={"verbose_name": "Учебная группа", "verbose_name_plural": "Учебные группы", "ordering": ["-name"]},
        )
    ]
