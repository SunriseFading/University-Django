from account.models import CustomUser


class Curator(CustomUser):
    class Meta:
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"
