from django import forms 
from .models import Post, Comment, Tag 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumb_image', 'file_upload']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']