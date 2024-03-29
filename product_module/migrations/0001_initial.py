# Generated by Django 5.0.3 on 2024-03-05 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='نام برند')),
                ('url_title', models.CharField(db_index=True, max_length=200, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برندها',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='نام دسته')),
                ('url_title', models.CharField(db_index=True, max_length=200, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'دسته',
                'verbose_name_plural': 'دسته ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام محصول')),
                ('Image', models.ImageField(upload_to='images/products', verbose_name='تصویر محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('short_description', models.CharField(max_length=300, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.productbrand', verbose_name='برند محصول')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.productcategory')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
