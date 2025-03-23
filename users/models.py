from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='почта', help_text='укажите почту')
    avatar = models.ImageField(upload_to='users/avatar', blank=True, null=True, verbose_name='аватар')
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='номер телефона')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
