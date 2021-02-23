from django import forms
from captcha.fields import ReCaptchaField
class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'password'}))
    confirm = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            return forms.ValidationError('Password and Confirm is not equal')

        values = {
            'username' :username,
            'password' : password
        }

        return values


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    captcha = ReCaptchaField()
    