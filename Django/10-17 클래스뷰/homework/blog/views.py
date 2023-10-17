from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm

def postlist(requset):
    posts = Post.objects.all()
    return render(requset, 'blog/postlist.html', {'posts' : posts})

def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment.objects.create(
                post = post,
                message = form.cleaned_data['message'],
                author = request.user
            )
            c.save()
        
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'blog/postdetail.html', context)


def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'blog/postlist.html', {'posts':posts})
# Create your views here.
