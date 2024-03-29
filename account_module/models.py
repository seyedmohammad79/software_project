from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='images/profile', verbose_name='تصویر پروفایل')
    email_active_code = models.CharField(max_length=6, verbose_name='کد فعالسازی', default='100000')
    email_active_url = models.CharField(max_length=100, db_index=True, verbose_name='عنوان فعالسازی ایمیل')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False

    def is_exists(self):
        if User.objects.filter(email=self.email):
            return True

        return False

    def get_user_info(self):
        return {'firstname': self.first_name,
                'lastname': self.last_name,
                'username': self.username,
                'password': self.password,
                'image': self.image,
                'email': self.email,
                'address': self.address}

    def update_user_info(self, first_name, last_name, username, password, image, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.image = image
        self.email = email
        self.address = address
        self.save()

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        return self.email
