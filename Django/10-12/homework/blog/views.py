from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def blog(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        db = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct()
    else:
        db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'blog/blog.html', context)

@login_required
def notice(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        db = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct()
    else:
        db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'blog/notice.html', context)

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'blog/post.html', context)

@login_required
def create(request):
    if request.method == 'POST':  # 만약 요청 메소드가 POST라면
        form = PostForm(request.POST, request.FILES)  # PostForm을 생성하고 요청 데이터와 파일을 전달하여 초기화
        if form.is_valid():  # 만약 폼이 유효하다면
            post = form.save()  # 폼을 저장하고 반환된 포스트 객체를 post 변수에 할당
            return redirect('post', pk=post.pk)  # post 뷰로 리디렉션하고 포스트 객체의 pk 값을 전달
    else:  # 요청 메소드가 POST가 아니라면
        form = PostForm()  # 빈 PostForm을 생성
        
    context = {
        'form' : form,
    }
    return render(request, 'blog/create.html', context)  # create.html 템플릿을 렌더링하여 응답 반환

@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form' : form,
    }
    return render(request, 'blog/create.html', context)

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    
    context = {
        'post' : post,
    }
    return render(request, 'blog/delete.html', context)