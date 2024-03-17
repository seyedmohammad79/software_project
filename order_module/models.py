from django.db import models
from account_module.models import User
from product_module.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return str(self.user)

    def total_price(self):
        total_amount = 0

        if self.is_paid:
            for detail_order in self.orderdetail_set:
                total_amount += detail_order.final_price
        else:
            for detail_order in self.orderdetail_set:
                total_amount += detail_order.count * detail_order.product.price


class OrderDetail(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='سفارش')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    count = models.IntegerField()
    final_price = models.IntegerField()
