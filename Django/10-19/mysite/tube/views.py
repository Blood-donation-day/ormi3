# write는 로그인 해야만
# update와 delete는 업로드한 사용자여야만

from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        qs = super().get_queryset()  # 부모 클래스(PostListView)의 get_queryset() 메서드 호출
        q = self.request.GET.get('q', '')  # GET 요청에서 'q' 파라미터 값을 가져옴, 값이 없으면 공백 문자로 설정
        if q:  # q 값이 존재하는 경우
            qs = qs.filter(title__icontains=q)  # title 필드에서 q 값을 포함하는 게시물 필터링
        return qs  # 필터링된 쿼리셋 반환
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'
    # context_object_name = 'tubes' 기본 모델의 이름을 따라감 >> post
    
    def form_valid(self, form):
        video = form.save(commit=False)
        video.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
            '''
            여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
            '''
            context = super().get_context_data(**kwargs)
            context['comment_form'] = CommentForm()
            return context
    
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)

    # def blog(request):   context로 전달
    # # db = Blog.objects.all()
    # context = {
    #     'db': db,
    # }
    # return render(request, 'blog/blog.html', context)

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'
    
    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')
    
    def test_func(self): # UserPassesTestMixin에 있고 test_func() 메서드를 오버라이딩, True, False 값으로 접근 제한
        return self.get_object().author == self.request.user


@login_required
def comment_new(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # commit=False는 DB에 저장하지 않고 객체만 반환
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('tube:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'tube/form.html', {
        'form': form,
    })

post_list = PostListView.as_view()
post_new = PostCreateView.as_view()
post_detail = PostDetailView.as_view()
post_edit = PostUpdateView.as_view()
post_delete = PostDeleteView.as_view()