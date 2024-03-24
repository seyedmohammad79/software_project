from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django_recaptcha.fields import ReCaptchaField

choice = (
    ('آذربایجان شرقی','آذربایجان شرقی'),
    ('آذربایجان غربی', 'آذربایجان غربی'),
    ('اردبیل', 'اردبیل'),
    ("اصفهان",'اصفهان'),
    ('البرز', 'البرز'),
    ('ایلام', 'ایلام'),
    ('بوشهر', 'بوشهر'),
    ('تهران', 'تهران'),
    ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'),
    ('خراسان جنوبی', 'خراسان جنوبی'),
    ('خراسان رضوی', 'خراسان رضوی'),
    ('خراسان شمالی', 'خراسان شمالی'),
    ('خوزستان', 'خوزستان'),
    ('زنجان', 'زنجان'),
    ('سمنان', 'سمنان'),
    ('سیستان و بلوچستان', 'سیستان و بلوچستان'),
    ('فارس', 'فارس'),
    ('قزوین', 'قزوین'),
    ('قم', 'قم'),
    ('کردستان', 'کردستان'),
    ('کرمان', 'کرمان'),
    ('کرمانشاه', 'کرمانشاه'),
    ('کهگیلویه و بویراحمد', 'کهگیلویه و بویراحمد'),
    ('گلستان', 'گلستان'),
    ('گیلان', 'گیلان'),
    ('لرستان', 'لرستان'),
    ('مازندران', 'مازندران'),
    ('مرکزی', 'مرکزی'),
    ('هرمزگان', 'هرمزگان'),
    ('همدان', 'همدان'),
    ('یزد', 'یزد'),
)


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل',
            'id': 'email'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'pass-key',
            'placeholder': 'رمزعبور'

        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'pass-key',
            'placeholder': 'تکرار رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور و تکرار کلمه عبور با یکدیگر مغایرت دارند')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'pass-key',
            'placeholder': 'رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class ForgotPassword(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder':'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class AuthenEmail(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل',
            'id': 'email'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPassword(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'pass-key',
            'placeholder': 'رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'pass-key',
            'placeholder': 'تکرار رمزعبور'
        }),
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
    email_active_code = forms.CharField(
        label='کد فعالسازی',
        widget=forms.TextInput(attrs={
            'placeholder': 'کد ارسال شده'
        }),
        validators=[
            validators.MaxLengthValidator(6)
        ]
    )
