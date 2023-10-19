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
      
# 안쓸거 같아. 일단 예시를 위해 작성
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']