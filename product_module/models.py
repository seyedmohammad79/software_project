from django.db import models
from django.utils.text import slugify


# Create your models here.


class ProductBrand(models.Model):
    name = models.CharField(max_length=200,db_index=True ,verbose_name='نام برند')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام دسته')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name ='دسته'
        verbose_name_plural = 'دسته ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, db_index=True)
    Image = models.ImageField(upload_to='images/products', verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند محصول')
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=300,null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(default="", null=False, db_index=True, max_length=200, blank=True, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

