from django.shortcuts import render
from .models import Post, Comment, Tag
from .forms import CommentForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def postlist(requset):
    posts = Post.objects.all().order_by('-pk')
    # get요청 오면(검색버튼) q로 필터링
    q = requset.GET.get('q', '')
    posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))

    return render(requset, 'blog/postlist.html', {'posts': posts})


# @login_required  클래스에서 적용 X >>  login_required함수안에 싸매서 사용.
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']
    success_url = reverse_lazy('postlist')


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload']
    success_url = reverse_lazy('postlist')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('postlist')


def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    # 댓글
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                post=post,
                message=form.cleaned_data['message'],
                author=request.user
            )
            c.save()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/postdetail.html', context)


def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'blog/postlist.html', {'posts': posts})


postcreate = login_required(PostCreate.as_view())
postupdate = login_required(PostUpdate.as_view())
postdelete = login_required(PostDelete.as_view())


# def posttest(request):
#     response = render(request, 'blog/postlist.html')
#     response.delete_cookie('sessionid')
#     return response
