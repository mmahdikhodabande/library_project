from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_pain = models.BooleanField(default=False, verbose_name='نهایی شده')
    pyment_data = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    # def calculate_total_price(self):
    #     total_amount = 0
    #     if self.is_pain:
    #         for order_detail in self.orderdetail_set.all():
    #             total_amount += order_detail.final_price * order_detail.count
    #     else:
    #         for order_detail in self.orderdetail_set.all():
    #             total_amount += order_detail.final_price * order_detail.count
    #     return total_amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی')
    count = models.IntegerField(verbose_name='تعداد محصول')

    def __str__(self):
        return self.order.user

    class Meta:
        verbose_name = 'توضیحات محصول'
        verbose_name_plural = 'توضیحات محصولات'
