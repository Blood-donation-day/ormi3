from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.db.models import Q

class PostList(ListView):
    
    model = Post
    ordering = '-pk'
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('q', '')
        
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(content__icontains=keyword))

        return queryset
    
class PostDetail(DetailView):
    
    model = Post
    template_name = 'blog/post_detail.html'