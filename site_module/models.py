from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='تلفن')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    about_us = models.TextField(verbose_name='متن درباره ما')
    site_logo = models.ImageField(upload_to='images/logo', verbose_name='لوگوی سایت')
    is_main_setting = models.BooleanField(verbose_name='تنطیمات اصلی سایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name
