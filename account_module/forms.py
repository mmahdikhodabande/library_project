from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'single-input-fields',
            'type': 'text',
            'placeholder': 'ایمیل '
        }),
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'single-input-fields',
            'type': 'password',
            'placeholder': 'رمز عبور'
        }),
        # validators=[
        #     validators.MaxLengthValidator(12),
        #     validators.MinLengthValidator(4),
        #
        # ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'single-input-fields',
            'type': 'password',
            'placeholder': 'مجددا رمز عبور خود را وارد کنید '
        }),
        # validators=[
        #     validators.MaxLengthValidator(12),
        #     validators.MinLengthValidator(4),
        #
        # ],
        # error_messages={'required': 'Please Enter your Name', }
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        len_pass = len(list(password))
        if len_pass < 4 or len_pass > 12:
            raise ValidationError('کلمه عبور باید بین 12 الی 4 کارکتر باشد ')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')

        


    # def clean_password(self):
    #     password = self.cleaned_data.get('password')



class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'single-input-fields',
            'type': 'text',
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'single-input-fields',
            'type': 'password',
            'placeholder': 'کلمه عبور '
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'single-input-fields',
            'type': 'text',
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'single-input-fields',
            'type': 'password',
            'placeholder': 'رمز عبور جدید خود را وارد کنید '
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'single-input-fields',
            'type': 'password',
            'placeholder': 'مجددا رمز عبور خود را وارد کنید '
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
