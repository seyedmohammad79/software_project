from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django_recaptcha.fields import ReCaptchaField


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    captcha = ReCaptchaField()

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        ValidationError('کلمه عبور و تکرار کلمه عبور با یکدیگر مغایرت دارند')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    captcha = ReCaptchaField()


class ForgotPassword(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPassword(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        ValidationError('کلمه عبور و تکرار کلمه عبور با یکدیگر مغایرت دارند')


class ActivateAccount(forms.Form):
    email_active_code = forms.IntegerField(
        label='کد فعالسازی',
        widget=forms.NumberInput(attrs={}),
        validators=[
            validators.MaxValueValidator(999999)
        ]
    )
