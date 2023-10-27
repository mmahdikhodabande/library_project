from django.db import models


# Create your models here.


class ContactUsModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    massage = models.TextField(verbose_name='متن پیام')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    response = models.TextField(null=True, blank=True, verbose_name='پاسخ ادمین')
    is_read_by_admin = models.BooleanField(default=True,verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        if self.full_name:
            return self.full_name
        return self.email

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'
