from django.db import models
from django.urls import reverse


# user_name = god    password = 8520

# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/ موجود')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصولات'


class Auther(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام نویسنده')
    url_name = models.CharField(max_length=100, verbose_name='نام در url')
    # about_auther = models.TextField(verbose_name='درباره نویسنده')
    # avatar = models.ImageField(upload_to='image/auther', null=True, blank=True, verbose_name='تصویر نویسنده')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'


class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    price = models.IntegerField(verbose_name='قیمت')
    amount_folio = models.IntegerField(verbose_name='تعداد صفحات')
    image = models.ImageField(upload_to='image/product', null=True, blank=True, verbose_name='تصویر')
    auther = models.ManyToManyField(Auther, db_index=True, verbose_name='نویسنده')
    authered = models.CharField(max_length=100,null=True, blank=True , verbose_name='نویسنده اش')
    publisher = models.CharField(max_length=100, null=True, blank=True, verbose_name='انتشارات')
    dragoman = models.CharField(max_length=100, null=True, blank=True, verbose_name='مترجم')
    description = models.TextField(db_index=True, verbose_name='توضیحات')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', db_index=True,
                                      verbose_name='دسته بندی')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / موجود')
    # add rating field...

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
