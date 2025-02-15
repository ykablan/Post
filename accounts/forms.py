from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı Adı' , max_length=100)
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput, max_length=100)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adı veya şifre hatalı')
        return super().clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Kullanıcı Adı' , max_length=100)
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput, max_length=100)
    password2 = forms.CharField(label='Şifre Doğrulama', widget=forms.PasswordInput, max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Şifreler uyuşmuyor')
        return password2