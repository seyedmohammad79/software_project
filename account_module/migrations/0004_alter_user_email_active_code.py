# Generated by Django 5.0.3 on 2024-03-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_alter_user_email_active_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_active_code',
            field=models.CharField(default='100000', max_length=6, verbose_name='کد فعالسازی'),
        ),
    ]