from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'contents', 'main_image']
        # fields = '__all__' #다 입력가능