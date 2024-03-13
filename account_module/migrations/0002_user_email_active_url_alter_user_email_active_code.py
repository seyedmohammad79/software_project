# Generated by Django 5.0.3 on 2024-03-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_active_url',
            field=models.CharField(db_index=True, default='abcd', max_length=100, verbose_name='عنوان فعالسازی ایمیل'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email_active_code',
            field=models.IntegerField(verbose_name='کد فعالسازی'),
        ),
    ]