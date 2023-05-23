from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_img', null=True, blank=True)
    done_tasks_count = models.PositiveSmallIntegerField(default=0)
    die_tasks_count = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
