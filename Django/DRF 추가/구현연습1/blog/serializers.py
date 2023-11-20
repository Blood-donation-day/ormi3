from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['username']
        
class BlogPostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = BlogPost
        fields =[
            'author',
            'title',
            'content',
        ]