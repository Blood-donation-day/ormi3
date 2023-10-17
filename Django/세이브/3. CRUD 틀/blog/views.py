from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q

# https://docs.djangoproject.com/en/4.2/ref/class-based-views/
# ListVeiw : https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/
# CreateView : https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/

#보통 모델이름 + 이름 붙여서 생성
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/변경.html'   / 기본 : post_list.html
    def get_queryset(self):
        queryset = super().get_queryset()
        #request의 GET파라미터에서 'q'를 가져옵니다.
        q = self.request.GET.get('q', '')
        
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return queryset
        

class PostDetail(DetailView):
    model = Post
    
class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')
    
class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')
    
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('postlist')

class PostTest(DetailView):
    model = Post
    
    def get(self, request):
        return HttpResponse('PostTest get')

    def post(self, request):
        return HttpResponse('PostTest post')
# Create your views here.


postlist = PostList.as_view() # as_view는 진입 메소드
postdetail = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = PostDelete.as_view()
test = PostTest.as_view()