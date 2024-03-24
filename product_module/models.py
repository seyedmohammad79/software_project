from django.db import models
from django.utils.text import slugify

from account_module.models import User


class ProductBrand(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام برند')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    @staticmethod
    def get_all_brandes():
        return ProductBrand.objects.all()

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام دسته')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/category', verbose_name='تصویر دسته', null=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته ها'

    @staticmethod
    def get_all_categories():
        return ProductCategory.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ForeignKey(ProductCategory, related_name='product_category', on_delete=models.CASCADE, db_index=True)
    Image = models.ImageField(upload_to='images/products', verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand, related_name='product_brand', on_delete=models.CASCADE, verbose_name='برند محصول')
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=300, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    create_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(default="", null=False, db_index=True, max_length=200, blank=True, unique=True, verbose_name='عنوان در url')
    count = models.IntegerField(default=0, verbose_name='موجودی')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.title


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید محصولات'
