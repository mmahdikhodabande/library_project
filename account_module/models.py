from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', verbose_name='پروفایل کاربر')
    active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی')
    address = models.CharField(max_length=150, verbose_name='آدرس')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    phone_number = models.IntegerField(null=True, blank=True, unique=True, verbose_name='شماره تماس')

    def __str__(self):
        if self.username:
            return self.username
        return self.email

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
