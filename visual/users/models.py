from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(unique=True, verbose_name='Email')
    username = models.CharField(max_length=50, verbose_name='Name', unique=True)
    registration_date = models.DateField(auto_now_add=True, verbose_name='Registration Date')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-registration_date',)

    def __str__(self):
        return self.email
