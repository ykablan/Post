from django import forms
from .models import Post, Comment
from django.contrib.auth import authenticate
# from django_recaptcha.fields import ReCaptchaField

class PostForm(forms.ModelForm):
    # captcha = ReCaptchaField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'checked']
        labels = {
            'title': 'Başlık',
            'content': 'İçerik',
            'publishing_date': 'Yayımlanma Tarihi',
            'checked' :' Servis Kapalı'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'publishing_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            #'checked': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
    
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('isim', None)
        self.ornekk = kwargs.pop('ornek', None)
        super().__init__(*args, **kwargs)
        name = forms.CharField()                
        self.fields['ornek'] = forms.CharField(initial=self.ornekk)
        if name is not None:
            self.fields['name']= forms.CharField(initial=self.name)

            if self.name:
                self.fields['name'].widget.attrs['readonly'] = True
            
        