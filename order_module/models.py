from django.db import models
from account_module.models import User
from product_module.models import Product


class Address(models.Model):
    region = models.CharField(null=True, blank=True, max_length=60, verbose_name='استان')
    city = models.CharField(max_length=60, verbose_name='شهر')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    house_number = models.CharField(max_length=30, verbose_name='پلاک')
    postal_code = models.CharField(max_length=15, verbose_name='کدپستی')

    def __str__(self):
        return f'{self.region} / {self.city}'

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def total_price(self):
        total_amount = 0

        if self.is_paid:
            for detail_order in self.orderdetail_set.all():
                total_amount += detail_order.final_price
        else:
            for detail_order in self.orderdetail_set.all():
                total_amount += detail_order.count * detail_order.product.price

        return total_amount

    class Meta:
        verbose_name = 'سبدخرید'
        verbose_name_plural = 'سبدهای خرید'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'
