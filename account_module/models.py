from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', verbose_name='پروفایل کاربر')
    active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی')
    address = models.CharField(max_length=150, verbose_name='آدرس')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')

    def __str__(self):
        if self.first_name:
            return self.get_full_name()
        return self.email

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
